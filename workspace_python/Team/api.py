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
    DATABASE_URL,
    echo=True
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
# 메인 페이지
# =========================================================

@app.get('/dsinside')
def main(
    request: Request,
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
                   where r.res_code = 1
                   ''')
        
        sql_menu = text('''
                        select 
                            menu_name, price
                            from restaurant r join menu m using(res_code)
                            where r.res_code = 1
                        ''')
        
        sql_rating = text('''
                            select round(avg(re.rating), 2) as rating
                            from restaurant r join review re using(res_code)
                            where res_code = 1
                        ''')
        
        result = session.exec(sql_res)
        
        result2 = session.exec(sql_menu)
        
        result3 = session.exec(sql_rating)
        
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

@app.get('/review/{res_code}')
def review(
    request: Request,
    res_code:int,
    session: Session = Depends(get_session)
):
    print('/review/{res_code} 실행 성공')
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
                mem.member_id,
                review_content,
                rev.rating,
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

@app.get('/review/{res_code}/{member_id}')
def review_add(request: Request,
               res_code: int,
               member_id: str,
               session: Session = Depends(get_session)):
    print('/review/{res_code}/{member_id} 실행 성공')
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
    
    print(member_info)
    return templates.TemplateResponse(
        request,
        'review_add.html',
        {
            'res_info': res_info,
            'member_info': member_info
        }
    )


@app.post('/review/{res_code}/{member_code}/add')
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
        url=f'/review/{res_code}',
        status_code=303
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
    
    member_id = request.session.get('member_id')
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
                'member_id':member_id
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

@app.get('/board')
def board(request:Request):
     return templates.TemplateResponse(
            request,
            'board.html'
        )
     

#글쓰기 버튼을 눌렀을때 이동하는 곳
     
@app.get('/board/write')
def board_write(request:Request):
    
  return templates.TemplateResponse(
             request,
             'board_write.html'
         )
  
  



# =========================================================
# 서버 실행
# =========================================================

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'api:app',
        port=8000,
        reload=True,
        host='0.0.0.0'
    )