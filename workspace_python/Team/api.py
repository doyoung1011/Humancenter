from fastapi import FastAPI,Cookie,Request,Response

from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlmodel import create_engine, Session, SQLModel
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

from datetime import datetime
from sqlalchemy import text

from passlib.context import CryptContext
from DTO.ReviewDTO import Review
from DTO.MemberDTO import Member
from DTO.BoardDTO import Board
from DTO.RestaurantDTO import Restaurant

from starlette.middleware.sessions import SessionMiddleware
# =========================================================
# FastAPI 기본 설정
# =========================================================

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key='Human123#'
) 

templates = Jinja2Templates(directory='templates/')



DATABASE_URL = 'mysql+pymysql://root:human123$@127.0.0.1:3306/human'

engine = create_engine(
    DATABASE_URL
    # echo=True
)


def get_session():
    with Session(engine) as session:
        yield session
        session.commit()


# =========================================================
# static 폴더 연결
# =========================================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# =========================================================
# 메인 페이지(가게 리스트 조회)
# =========================================================

@app.get('/dsinside')
def main_res_page(
    request: Request,
    session: Session = Depends(get_session)):
    print('/dsinside 실행 성공')
    
    res_list = []
    popular_list = []
    
    try:
        sql_res = text('''
                   select 
                   res_code, res_name, category,
                   (
                       select
                            menu_name
                        from Menu m
                        where m.res_code = r.res_code
                        limit 1
                   ) as menu_name,
                   (
                       select
                            price
                        from Menu m
                        where m.res_code = r.res_code
                        limit 1
                   ) as price,
                   address,
                   (
                       select
                            count(*)
                        from review rev
                        where rev.res_code = r.res_code
                   ) as review_count,
                   (
                       select
                            round(avg(rating), 2)
                        from review rev
                        where rev.res_code = r.res_code
                   ) as rating
                   from restaurant r
                   ''')
        
        sql_popular = text('''
                           select res_name,
                           (
                               select
                                    round(avg(rating), 2)
                                    from review rev
                                    where rev.res_code = r.res_code
                           ) as rating,
                           (
                                select
                                     count(*)
                                     from review rev
                                     where rev.res_code = r.res_code
                                 ) as review_count
                           from restaurant r
                           order by rating desc
                           limit 4
                           ''')
        
        # 가게 정보 가져오기.
        result = session.exec(sql_res)
        res_list = result.mappings().fetchall()
        
        # 인기 가게 가져오기.
        result_popular = session.exec(sql_popular)
        popular_list = result_popular.mappings().fetchall()
              
    except Exception as e:
        # 출력 확인용
        # print('res_code:', res_code)
        # print('res_info:', res_info)
        # print('res_list:', res_list)
        print('메인 페이지 에러:', e)
    
    # 웰컴 팝업을 스위치 처럼 사용하기 위해
    # 최초의 값은 False로 설정한다
    should_show_welcome_popup = request.session.get(
        'login_welcome_popup',
         False)

    return templates.TemplateResponse(
        request,
        'restaurant_list.html',
        {
        'res_list': res_list,
        'popular_list': popular_list,
        'should_show_welcome_popup': should_show_welcome_popup
        }
    )
    
# =========================================================
# 가게 등록 페이지
# =========================================================

@app.get('/dsinside/add')
def res_add(
    request: Request,
    session: Session = Depends(get_session)
):
    member_id = request.session.get('member_id')

    if member_id is None:
        return RedirectResponse(
            url='/login',
            status_code=303
        )

    member_info = None

    try:
        sql_member = text('''
            SELECT member_code, name
            FROM member
            WHERE member_id = :member_id
        ''')

        member = session.exec(
            sql_member,
            params={
                'member_id': member_id
            }
        )

        member_info = member.mappings().fetchone()

    except Exception as e:
        print('member_id:', member_id)
        print('맛집 등록 페이지 이동 오류:', e)

    return templates.TemplateResponse(
        request,
        'restaurant_add.html',
        {
            'member_info': member_info
        }
    )


@app.post('/dsinside/add/api')
def res_list_add(
    request: Request,

    # Restaurant
    res_name: str = Form(),
    category: int = Form(),
    address: str = Form(),
    res_pnum: str = Form(),
    open_time: str = Form(),
    close_time: str = Form(),

    # Menu
    menu_name: list[str] = Form(default=[]),
    price: list[str] = Form(default=[]),

    # Closed Days
    c_code: list[int] = Form(default=[]),

    session: Session = Depends(get_session)
):
    print('dsinside/add/api 실행 성공')

    try:

        # =====================================================
        # 1. 로그인 회원 확인
        # =====================================================

        member_id = request.session.get('member_id')

        if member_id is None:
            print('로그인 정보가 없습니다.')

            return RedirectResponse(
                url='/login',
                status_code=303
            )

        # member_id를 이용해서 member_code 가져오기
        sql_member = text('''
            SELECT member_code
            FROM member
            WHERE member_id = :member_id
        ''')

        result_member = session.exec(
            sql_member,
            params={
                'member_id': member_id
            }
        )

        member = result_member.mappings().fetchone()

        if member is None:
            print('회원 정보를 찾을 수 없습니다.')

            return RedirectResponse(
                url='/login',
                status_code=303
            )

        member_code = member['member_code']

        print('member_code:', member_code)


        # =====================================================
        # 2. Restaurant 등록
        # =====================================================

        sql_res = text('''
            INSERT INTO restaurant
            (
                member_code,
                category,
                res_name,
                address,
                res_pnum,
                open_time,
                close_time
            )
            VALUES
            (
                :member_code,
                :category,
                :res_name,
                :address,
                :res_pnum,
                :open_time,
                :close_time
            )
        ''')

        restaurant_data = {
            'member_code': member_code,
            'category': category,
            'res_name': res_name,
            'address': address,
            'res_pnum': res_pnum,
            'open_time': open_time,
            'close_time': close_time
        }

        result = session.exec(
            sql_res,
            params=restaurant_data
        )

        res_code = result.lastrowid

        print('등록된 res_code:', res_code)


        # =====================================================
        # 3. Menu 등록
        # =====================================================

        sql_menu = text('''
            INSERT INTO menu
            (
                res_code,
                menu_name,
                price
            )
            VALUES
            (
                :res_code,
                :menu_name,
                :price
            )
        ''')

        menu_count = 0

        for i in range(len(menu_name)):

            name = menu_name[i].strip()

            # 메뉴명이 비어 있으면 건너뜀
            if not name:
                continue

            # 가격이 비어 있으면 오류
            if i >= len(price) or not price[i].strip():
                raise ValueError(
                    f'{i + 1}번째 메뉴의 가격을 입력해주세요.'
                )

            menu_price = int(price[i])

            session.exec(
                sql_menu,
                params={
                    'res_code': res_code,
                    'menu_name': name,
                    'price': menu_price
                }
            )

            menu_count += 1


        # 메뉴가 하나도 없으면 등록 취소
        if menu_count == 0:
            raise ValueError(
                '메뉴를 한 가지 이상 입력해주세요.'
            )


        # =====================================================
        # 4. 휴무일 등록
        # =====================================================

        sql_closed_day = text('''
            INSERT INTO res_c_day_bridge
            (
                res_code,
                c_code
            )
            VALUES
            (
                :res_code,
                :c_code
            )
        ''')

        for code in c_code:

            session.exec(
                sql_closed_day,
                params={
                    'res_code': res_code,
                    'c_code': code
                }
            )


        # =====================================================
        # 5. 전체 등록 완료
        # =====================================================

        session.commit()

        print('맛집 등록 완료')

        return RedirectResponse(
            url='/dsinside',
            status_code=303
        )


    except Exception as e:

        print('맛집 등록 처리 오류:', e)

        session.rollback()

        return RedirectResponse(
            url='/dsinside/add',
            status_code=303
        )

# =========================================================
# 메인 페이지(였던 것)
# =========================================================

@app.get('/dsinside/res_code={res_code}')
def main(
    request: Request,
    res_code: int,
    session: Session = Depends(get_session)):
    
    res_info = []
    menu_info = []
    rating_info = 0.0
    
    # where절 조건 리스트 전체 조회하는 페이지에서 넘어갈 때 res_code 들고 오게끔 수정.
    try:
        sql_res = text('''
                   select 
                   r.res_code res_code, r.res_name, r.rating, r.address, r.open_time, r.close_time, r.res_pnum,
                   c.dow dow
                   from restaurant r join menu m on r.res_code = m.res_code
                   join res_c_day_bridge rc on r.res_code = rc.res_code
                   join closed_days c on rc.c_code = c.c_code
                   where r.res_code = :res_code
                   ''')
        
        sql_menu = text('''
                        select 
                            menu_name, price
                            from restaurant r join menu m using(res_code)
                            where r.res_code = :res_code
                        ''')
        
        sql_rating = text('''
                            select round(avg(re.rating), 2) as rating
                            from restaurant r join review re using(res_code)
                            where res_code = :res_code
                        ''')
        
        result = session.exec(sql_res, params={'res_code': res_code})
        
        result2 = session.exec(sql_menu, params={'res_code': res_code})
        
        result3 = session.exec(sql_rating, params={'res_code': res_code})
        
        res_info = result.mappings().fetchone()
        
        menu_info = result2.mappings().fetchall()
        
        rating_info = result3.mappings().fetchone()
        
    except Exception as e:
        # 출력 확인용
        # print('res_code:', res_code)
        # print('res_info:', res_info)
        print('메인 페이지 에러:', e)
    
    
    return templates.TemplateResponse(
        request,
        'main.html',
        {
        'res_info': res_info,
        'menu_info': menu_info,
        'rating_info': rating_info
        }
    )


# =========================================================
# 로그인 페이지
# =========================================================

@app.get('/login')
def login(request: Request):
    return templates.TemplateResponse(
        request,
        'login.html'
    )


# =========================================================
# 검색 페이지
# =========================================================

@app.get('/search')
def search(request: Request):
    return templates.TemplateResponse(
        request,
        'search.html'
    )


# =========================================================
# 로그인 처리
# 로그인 구현 성공, 로그인할때 세션에 이름도 전달해야함
# =========================================================

def verify(orig, hashed):
    return ctx_pw.verify(orig, hashed)

@app.post('/api/login')
def _login(
   request:Request,
   member_id:str=Form(),
   member_pw:str=Form(),
   session: Session = Depends(get_session)   
):
   
       
    sql=text('''
             select *
             from member
             where member_id=:member_id
             
             ''')
    # 세션에 id에 대한 정보를 담고
    
    result=session.exec(
               sql,
               params={
                   'member_id':member_id,
                   
               }
           )
    
    member=result.mappings().fetchone()
    
    #  아이디 검증
    if member is None:
          return RedirectResponse(
                url='/login',
                status_code=303
            )
    # 비밀번호 검증
    
    if not verify(member_pw,member['member_pw']):
            return RedirectResponse(
                        url='/login',
                        status_code=303
                    )
    
    request.session['member_id']=member['member_id']
    request.session['name']=member['name']
    request.session['member_code'] = member['member_code']
    request.session['login_welcome_popup'] = True
    
   
    
    return RedirectResponse(
           url='/dsinside',
           status_code=303
       )
    
    
   

    
    
# =========================================================
#  로그아웃 처리- 아직 구현중입니다
# 
# =========================================================

 
 # 로그아웃 
@app.get('/logout')
def logout(request:Request):
    
    request.session.clear()
    
    return RedirectResponse(
               url='/dsinside',
               status_code=303
           )
       

# =========================================================
# 식당 정보 수정
# =========================================================

@app.get('/restaurant/update')
def restaurantUpdate(request: Request):
    return templates.TemplateResponse(
        request,
        'update.html'
    )


# =========================================================
# 리뷰 전체 조회
# =========================================================

@app.get('/review/res_code={res_code}')
def review(
    request: Request,
    res_code:int,
    session: Session = Depends(get_session)
):
    print('/review/res_code={res_code} 실행 성공')
    print('res_code:', res_code)
    res_info = []
    review_list = []
    rating_info = 0.0
    
    try:
        sql = text('''
                   select *
                   from restaurant
                   where res_code = :res_code
                   ''')
        
        sql_review = text('''
            select
                mem.member_id as member_id,
                res_code,
                review_code,
                review_content,
                rev.rating as rating,
                DATE_FORMAT(review_time, "%Y.%m.%d") AS review_time
            FROM restaurant as r join review AS rev using(res_code)
            JOIN member AS mem on rev.member_code = mem.member_code
            where res_code = :res_code
        ''')
        
        sql_review_cnt = text('''
                              select
                                    count(*) as count
                                    FROM restaurant as r join review AS rev using(res_code)
                                    JOIN member AS mem on rev.member_code = mem.member_code
                                    where res_code = :res_code
                              ''')
        
        sql_rating = text('''
                            select round(avg(re.rating), 2) as rating
                            from restaurant r join review re using(res_code)
                            where res_code = :res_code
                        ''')
        
        result = session.exec(sql, params ={'res_code': res_code})
        res_info = result.mappings().fetchone()
        
        result_review = session.exec(sql_review, params = {'res_code': res_code})
        review_list = result_review.mappings().fetchall()
        
        result_review_count = session.exec(sql_review_cnt, params = {'res_code': res_code})
        review_count = result_review_count.mappings().fetchone()
        
        result_rating = session.exec(sql_rating, params={'res_code': res_code})
        rating_info = result_rating.mappings().fetchone()

        # print('리뷰 조회 결과:', review_list)
        
    except Exception as e:
        # print(res_info)
        # print(review_list)
        print('리뷰 조회 에러:', e)
        
    # request.session['res_code'] = res_info['res_code']

    return templates.TemplateResponse(
        request,
        'review.html',
        {
            'res_info': res_info,
            'review_list': review_list,
            'review_count': review_count,
            'rating_info': rating_info
        }
    )



# =========================================================
# 리뷰 작성 페이지
# =========================================================

@app.get('/review/res_code={res_code}/member_id={member_id}')
def review_add(request: Request,
               res_code: int,
               member_id: str,
               session: Session = Depends(get_session)):
    print('/review/res_code={res_code}/member_id={member_id} 실행 성공')
    member_info = []
    try:
        sql = text('''
                   select res_code, res_name
                   from restaurant
                   where res_code = :res_code
                   ''')
        
        sql_member = text('''
                            select member_code, name
                            from member
                            where member_id = :member_id
                            ''')
        
        result = session.exec(sql, params = {'res_code': res_code})
        res_info = result.mappings().fetchone()
        
        member = session.exec(sql_member, params = {'member_id': member_id})
        member_info = member.mappings().fetchone()
        
    except Exception as e:
        print('리뷰 작성 페이지 이동 오류:', e)
        
    if member_id == 'None':
              return RedirectResponse(
                    url='/login',
                    status_code=303
                )
    
    # print(member_info)
    return templates.TemplateResponse(
        request,
        'review_add.html',
        {
            'res_info': res_info,
            'member_info': member_info
        }
    )
    
@app.post('/review/res_code={res_code}/{member_code}/add')
def review_add2(
    res_code: int,
    member_code: int,
    review: Review = Form(),
    session: Session = Depends(get_session)
):
    print("/review/add 실행 성공")
    print("review:", review)

    try:
        sql = text('''
            INSERT INTO review (
                res_code,
                member_code,
                review_content,
                rating,
                review_time
            )
            VALUES (
                :res_code,
                :member_code,
                :review_content,
                :rating,
                :review_time
            )
        ''')

        session.exec(
            sql,
            params={
                'res_code': res_code,
                'member_code': member_code,
                'review_content': review.review_content,
                'rating': review.rating,
                'review_time': datetime.now()
            }
        )
        
    except Exception as e:
        # print('res_code:', review.res_code)
        # print('member_code:', review.member_code)
        print('리뷰 등록 에러:', e)
        
    # print(res_code)
    
    return RedirectResponse(
        url=f'/review/res_code={res_code}',
        status_code=303
    )

# =========================================================
# 리뷰 수정 페이지
# =========================================================

@app.get('/review/review_code={review_code}')
def review_update(request: Request,
               review_code: int,
               session: Session = Depends(get_session)):
    print('/review/review_code={review_code} 실행 성공')
    print('여긴 리뷰 수정 페이지')
    member_id = request.session.get('member_id')
    review_info = []
    try:
        sql = text('''
                   select review_code, res_code, member_code, review_content, rating
                   from review
                   where review_code = :review_code
                   ''')
        
        sql2 = text('''
                    select res_name
                    from restaurant
                    where res_code = :res_code
                    ''')
        
        sql3 = text('''
                    select member_id
                    from member
                    where member_code = :member_code
                    ''')
        
        result = session.exec(sql, params = {'review_code': review_code})
        review_info = result.mappings().fetchone()
        
        result2 = session.exec(sql2, params = {'res_code': review_info.res_code})
        res = result2.mappings().fetchone()
        
        result3 = session.exec(sql3, params = {'member_code': review_info.member_code})
        chk = result3.mappings().fetchone()
        
    except Exception as e:
        print('리뷰 수정 페이지 이동 오류:', e)
        
    if member_id is None:
              return RedirectResponse(
                    url='/login',
                    status_code=303
                )
    elif member_id != chk.member_id:
        # print(member_id, type(member_id))
        # print(chk, type(chk))
        print('해당 리뷰 작성자가 아닙니다.')
        return RedirectResponse(
                    url='/dsinside',
                    status_code=303
                ) 
    
    # print(member_info)
    
    return templates.TemplateResponse(
        request,
        'review_update.html',
        {
            'review_info': review_info,
            'res': res,
            'chk': chk
        }
    )
    
@app.post('/review/review_code={review_code}/update')
def review_update_exec(review_code : int,
                       review: Review = Form(),
                       session: Session = Depends(get_session)):
    print('/review/review_code={review_code}/update 실행 성공')
    try:
        sql = text('''
                   update review
                   set review_content = :review_content,
                       rating = :rating
                   where review_code = :review_code
                   ''')
        
        session.exec(sql, params = { 'review_code': review_code,
                           'review_content': review.review_content,
                           'rating': review.rating})
        
        session.commit()
    
    except Exception as e:
        print('에러가 발생했습니다',e)
        session.rollback()
    
    return RedirectResponse(               
                        url=f'/review/res_code={review.res_code}',
                        status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다
                       )        
    
# =========================================================
# 리뷰 삭제
# =========================================================

@app.post('/review/res_code={res_code}/review_code={review_code}/delete')
def review_list_delete_review(
    res_code: int,
    review_code : int,
    session:Session=Depends(get_session)):
    print('/review/res_code={res_code}/review_code={review_code}/delete 실행 성공')
  
    try:
      sql=text('''
                delete from review
                where review_code=:review_code    
                ''')
      
      session.exec(
            sql,
            params={'review_code': review_code}
        )
      
      session.commit()
      
    except Exception as e:
        print('에러가 발생했습니다',e)
        session.rollback()
          
    return RedirectResponse(               
                    url=f'/review/res_code={res_code}',
                    status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다
                   )

# =========================================================
# 회원가입 페이지
# =========================================================

@app.get('/signup')
def sign_up(request: Request):
    return templates.TemplateResponse(
        request,
        'sign_up.html'
    )


# =========================================================
# 회원가입 처리
# =========================================================
ctx_pw = CryptContext(
    schemes=['argon2'],
    deprecated='auto'
)

def crypt(txt):
    return ctx_pw.hash(txt)


@app.post('/api/signup')
def _signup(
    member: Member = Form(),
    session: Session = Depends(get_session)
):
    print('/api/signup 실행 성공')
    print('member:', member)

    hashed = crypt(member.member_pw)

    try:
        sql = text('''
            INSERT INTO member (
                name,
                member_id,
                member_pw,
                member_pnum
            )
            VALUES (
                :name,
                :member_id,
                :member_pw,
                :member_pnum
            )
        ''')

        session.exec(
            sql,
            params={
                'name': member.name,
                'member_id': member.member_id,
                'member_pw': hashed,
                'member_pnum': member.member_pnum
            }
        )
    except Exception as e:
        print('회원가입 에러:', e)

    return RedirectResponse(
        url='/login',
        status_code=303
    )


# =========================================================
# 마이페이지
# =========================================================


@app.get('/mypage')
def mypage(request: Request):
    
    login_chk=request.session.get('member_id')
    
    if not login_chk:
        return RedirectResponse(
                url='/dsinside',
                status_code=303
            )
        
    return templates.TemplateResponse(
            request,
            'mypage.html',
            {
                'member_id': login_chk
            }
        )
    
# =========================================================
# 마이페이지에서 내가 쓴 리뷰를 모아둔 공간임
# =========================================================        
        
   

@app.get('/mypage/reviews')
def reviews(request: Request, session: Session = Depends(get_session)):
    
    print("리뷰 조회 사이트 들어와졌니?")
    
    # 세션에서 로그인 여부 체크하고 
    logChk = request.session.get('member_id')
    print("logChk:", logChk)
    print("세션 전체:", request.session)
    
    if logChk:       
       
        sql = text('''
         SELECT *
         FROM review rv
         JOIN member m  using(member_code)
         left join restaurant r using(res_code)
         where m.member_id=:member_id;
         ''')
        
      
        result=session.exec(
            sql,
            params={'member_id': logChk}
        )
         
   
        review_list=result.mappings().fetchall()
        print("review_list:", review_list)
        
        return templates.TemplateResponse(
                  request,
                  'myreview_list.html',
                  {
                      'review_list': review_list
                  }
              )
          
    else:
    
        return RedirectResponse(
            url='/login',
            status_code=303
        )

# 마이 페이지에서 내가 쓴 글 삭제하는 부분        
@app.post('/review/delete')

def delete_review(
    review_code : int=Form(),
    session:Session=Depends(get_session)):
    
  
    try:
      sql=text('''
                delete from review
                where review_code=:review_code    
                ''')
      
      session.exec(
            sql,
            params={'review_code': review_code}
        )
      session.commit()
      
    except Exception as e:
        print('에러가 발생했습니다',e)
        session.rollback()
          
    return RedirectResponse(               
                    url='/mypage/reviews',
                    status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다
                   )    
                     
      


# ========== 2026-09-12 마이 페이지 업데이트부분========= 


@app.get('/mypage/update')
def mypage_updatepage(
    request: Request,
    session: Session = Depends(get_session)
):

    # 세션에 id가 담겨있음
    member_id = request.session.get('member_id')

    if member_id:
        sql = text('''
            SELECT *
            FROM member
            WHERE member_id = :member_id
        ''')

        result = session.exec(
            sql,
            params={
                'member_id': member_id
            }
        )

        member = result.mappings().fetchone()

        return templates.TemplateResponse(
            request,
            'mypage_update.html',
            {
                'member': member
            }
        )

    else:
        return RedirectResponse(
            url='/dsinside',
            status_code=303
        )
   


    
    
# 내정보 수정, 이름과 전화번호까지만 수정가능한 설정,
# 세션에 있는거
@app.post('/api/mypage/update')
def _update(
    request:Request,
    name:str=Form(),
    member_pnum:str=Form(), 
    session: Session = Depends(get_session)
):
    
    login_id = request.session.get('member_id')
    try:
        session.exec(
            text('''
                UPDATE member
                SET
                    name = :name,
                    member_pnum = :member_pnum
                    WHERE member_id = :member_id
            '''),
            params={
                'name': name,
                'member_pnum':member_pnum,
                'member_id': login_id
            }
        )

        session.commit()
        
        
    except Exception as e:
        print('에러 발생 수정요망', e)

    return RedirectResponse(
        url='/mypage/update',
        status_code=303
    ) 
  
        


# =========================================================
# 관리자 페이지
# 회원 전체 조회 및 관리
# =========================================================

@app.get('/manager')
def manager(
    request: Request,
    session: Session = Depends(get_session)
):
    member = []

    try:
        sql = text('''
            SELECT *
            FROM member
        ''')

        result = session.exec(sql)
        member = result.mappings().fetchall()

        print('회원 전체 조회:', member)

    except Exception as e:
        print(f"데이터베이스 조회 중 에러 발생: {e}")

    return templates.TemplateResponse(
        request,
        'admin_member.html',
        {
            'member': member
        }
    )


# =========================================================
# 관리자 페이지
# 회원 상세 조회
# =========================================================

@app.get('/detail')
def detail(
    request: Request,
    member_id: str,
    session: Session = Depends(get_session)
):
    member = None

    try:
        sql = text('''
            SELECT *
            FROM member
            WHERE member_id = :member_id
        ''')

        result = session.exec(
            sql,
            params={
                'member_id': member_id
            }
        )

        member = result.mappings().fetchone()

        print('fetchone 결과:', member)

    except Exception as e:
        print('상세조회 에러 발생:', e)

    return templates.TemplateResponse(
        request,
        'detail.html',
        {
            'member': member
        }
    )

# =========================================================
# 게시판라우팅
# =========================================================

@app.get('/board/')
def board(request:Request,
          session: Session = Depends(get_session)):
    
    board_list = []
    
    try:
        sql = text('''
                   select b.board_code as board_code, b.board_title as board_title,
                   m.member_id as member_id, date_format(board_time, "%Y.%m.%d") as board_time, b.view_count as view_count
                   from board as b join member as m using(member_code)
                   ''')
        
        result = session.exec(sql)
        board_list = result.mappings().fetchall()
    
    except Exception as e:
        print('게시판 이동 오류:', e)
        
        
    return templates.TemplateResponse(
            request,
            'board.html',
            {
                'board_list': board_list
            }
        )
     
# =========================================================
# 글쓰기 버튼을 눌렀을때 이동하는 곳
# =========================================================

@app.get('/board/member_id={member_id}')
def board_write(request:Request,
                member_id : str,
                session: Session = Depends(get_session)):
    print('/board/member_id={member_id} 실행 성공')
    
    member_info = []
    try:    
        sql = text('''
                            select member_code, name
                            from member
                            where member_id = :member_id
                            ''')
        
        result = session.exec(sql, params = {'member_id': member_id})
        member_info = result.mappings().fetchone()
        
            
    except Exception as e:
        print('게시판 등록 페이지 이동 오류:', e)
    
    print(member_id)
    return templates.TemplateResponse(
                request,
                'board_write.html',
                {
                    'member_info': member_info
                }
            )

@app.post('/board/member_id={member_id}/add')
def board_write_insert(member_id: str,
                       board: Board = Form(),
                       session: Session = Depends(get_session)):
    print('/board/member_id={member_id}/add 실행 성공')
    print('board', board)
    
    try:
        sql = text('''
                   insert into Board(
                       member_code,
                       board_cate,
                       board_title,
                       board_content,
                       view_count,
                       board_time
                   )
                   values (
                       :member_code,
                       :board_cate,
                       :board_title,
                       :board_content,
                       :view_count,
                       :board_time
                   )
                   ''')
        
        sql_writer = text('''
                          select member_code, name
                          from member
                          where member_id = :member_id
                          ''')
        
        result_writer = session.exec(sql_writer, params = {'member_id': member_id})
        writer_info = result_writer.mappings().fetchone()
        
        session.exec(sql, params = {'member_code': writer_info.member_code,
                                    'board_cate': board.board_cate,
                                    'board_title': board.board_title,
                                    'board_content': board.board_content,
                                    'view_count': 0,
                                    'board_time': datetime.now()} )
        
    except Exception as e:
        print('게시판 등록 처리 오류', e)
        
    return RedirectResponse(
            url='/board',
            status_code=303
        )

# =========================================================
# 게시판 상세 페이지
# =========================================================


@app.get('/board/board_code={board_code}')
def board_detail(request: Request,
    board_code : int,
    session: Session = Depends(get_session)):
    print('/board/board_code={board_code} 실행 성공')
    board_info = []
    comment_list = []
    comment_cnt = 0
    try:
        sql = text('''
                   select board_code, member_code, member_id, name, board_cate,
                   board_title, board_content, view_count,
                   date_format(board_time, '%Y.%m.%d %H:%i') as board_time
                   from board b join member m using(member_code)
                   where board_code = :board_code
                   ''')
        
        sql_comment = text('''
                            with recursive comment_recu as (
                            select
                                comment_code,
                                member_code,
                                member_id,
                                comment_content,
                                date_format(comment_time, '%Y.%m.%d %H:%i') as comment_time,
                                lpad(member_id, length(member_id), ' '),
                                1 as level,
                                cast(member_id as char(200)) as sort_key
                            from
                                comment c join member m using(member_code)
                            where
                                parent_comment_code is null
                                and board_code = :board_code
                            union all
                            select
                                c.comment_code as comment_code,
                                m.member_id as member_id,
                                c.comment_content as comment_content,
                                c.parent_comment_code as parent_comment_code,
                                date_format(c.comment_time, '%Y.%m.%d %H:%i') as comment_time,
                                lpad(m.member_id, (cr.level * 4)+ length(m.member_id), ' '),
                                cr.level + 1 as level,
                                concat(cr.sort_key, '-', cast(m.member_id as char(200))) as sort_key
                            from
                                comment c join member m using(member_code)
                            join comment_recu cr on
                                c.parent_comment_code = cr.comment_code
                            )
                            select
                                *
                            from
                                comment_recu
                            order by
                                sort_key;
                           ''')
        
        sql_comment_cnt = text('''
                               select count(*) as count
                               from comment
                               where board_code = :board_code
                               ''')
        
        result = session.exec(sql, params = {'board_code': board_code})
        board_info = result.mappings().fetchone()
        
        result_comment = session.exec(sql_comment, params = {'board_code': board_code})
        comment_list = result_comment.mappings().fetchall()
        
        result_comment_cnt = session.exec(sql_comment_cnt, params={'board_code': board_code})
        comment_cnt = result_comment_cnt.mappings().fetchone()
                
    except Exception as e:
        print('상세 페이지 이동 오류:', e)    
    
    return templates.TemplateResponse(
            request,
            'board_detail.html',
            {
                'board_info': board_info,
                'comment_list': comment_list,
                'comment_cnt': comment_cnt
            }            
        )
     

# =========================================================
# 서버 실행
# =========================================================

# =========================================================
# 비밀번호 재설정
# =========================================================

@app.get('/find_pw')
def find_fw(request: Request):
    return templates.TemplateResponse(
        request,
        'find_pw.html'
    )


new_pw = CryptContext(
    schemes=['argon2'],
    deprecated='auto'
)


@app.post('/api/find_pw')
def resetPassword(
    request: Request,
    member: Member = Form(),
    session: Session = Depends(get_session)
):
    print('/api/pw 실행 성공')
    print('member:', member)

    hashed = new_pw.hash(member.member_pw)

    try:
        session.exec(
            text('''
                UPDATE member
                SET member_pw = :new_pw
                WHERE member_id = :member_id
            '''),
            params={
                'new_pw': hashed,
                'member_id': member.member_id
            }
        )
        session.commit()
        print('성공?')

    except Exception as e:
        print(f"비밀번호 재설정 중 에러가 발생함: {e}")

    return RedirectResponse(url='/login', status_code=303)


# =========================================================
# 사이트 안내 / 약관 / 개인정보처리방침
# =========================================================

@app.get('/soge')
def notice(request: Request):
    return templates.TemplateResponse(
        request,
        'soge.html'
    )


@app.get('/terms')
def terms(request: Request):
    return templates.TemplateResponse(
        request,
        'terms.html'
    )


@app.get('/privacy_policy')
def privacy_policy(request: Request):
    return templates.TemplateResponse(
        request,
        '/privacy_policy.html'
    )


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'api:app',
        port=8000,
        reload=True,
        host='192.168.0.25'
    )