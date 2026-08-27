
from fastapi import Request,Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlmodel import create_engine,Session,SQLModel
from fastapi import FastAPI,Depends

from sqlalchemy import text
from typing import Optional
from DTO.EmpDTO import Emp3 #이를 함으로써 create table을 수행가능함
import multipart

# 사용 예시
# decoder = multipart.MultipartDecoder(body, boundary)


app=FastAPI()
templates = Jinja2Templates(directory='templates/')  
# Session

DATABASE_URL='mysql+pymysql://root:human123$@127.0.0.1:3306/human'
engine=create_engine(DATABASE_URL,echo=True)
emp3=[]
# 기초적인 틀은 잡아두기
def get_session():
    with Session(engine) as session:
        yield session
        session.commit()
        
@app.on_event('startup')
def on_startup():
    SQLModel.metadata.create_all(engine)   
     
# 전체 조회부터 하자
@app.get('/emp/list')
def emp_list(
    request:Request,
    session:Session=Depends(get_session)
    
):
#   try문 
    try:
        # text: sql문을 실행하기 전에 미리 컴파일 해둔다.
        sql=text('''            
            select *
            from emp3
            
        ''')
        result=session.execute(sql)
        emp3=result.mappings().fetchall()
        print(emp3)
             
    except Exception as e:
        print(e)
   
    return templates.TemplateResponse(request,'emp_list.html',{
            'emp3':emp3
        })
    
 # 추가페이지로 이동중..
# @app.get('/add')
# def _add(request:Request):
#     print('이동중(성공했니?)')
      
#     return templates.TemplateResponse(request,'add.html')    
# empno(사번에 a태그를 줘서 이동하는 구조로 설계)

# @app.post('/emp/add')
# def add(
#     request:Request,
#     empno: int=Form(),
#     ename: str=Form(),
#     job:str=Form(),
#     mgr:Optional[int]=Form(None),
#     hiredaste:str=Form(),
#     sal:float=Form(),   
#     comm:Optional[int]=Form(None),
#     deptno: int=Form(),
    
#     session:Session=Depends(get_session),
    
# ):   
#     try :
#         sql = text('''
#             insert into emp3 
#             (empno, ename, job, mgr, hiredaste, sal, comm, deptno)
#             values (:empno, :ename, :job, :mgr, :hiredaste, :sal, :comm, :deptno )
#         ''')

#         session.execute(sql, {
#             "empno" : empno,
#             "ename" : ename,
#             "job" : job,
#             "mgr" : mgr,
#             "hiredaste" : hiredaste,
#             "sal" : sal,
#             "comm" : comm,
#             "deptno" : deptno
#         })

#         session.commit()
    
#     except Exception as e :
#         print(e)

# detail 페이지부터 다시 접근하기
# select문에 where이 where=deptno로 접근하면됨

@app.get('/detail')
def detail(
    
    request:Request,
    empno:int,
    # 의존성 주입
    session:Session=Depends(get_session)):

     try :
         sql=session.execute(text('''
            select *
            from emp3
            where empno=:empno             
         '''),{'empno':empno})
        #  rows=result.fetchone()
         a=sql.mappings().fetchone()
       
         print('fetchone결과:',a)
           
     except Exception as e :
            print(e)        
    
    
     return templates.TemplateResponse(request,'detail.html',{'emp3':a})

@app.get('/update')
def _update(
    
    request:Request,
    empno:int,
    # 의존성 주입
    session:Session=Depends(get_session)):
     print("함수 작동확인?")

     try :
         sql=session.execute(text('''
            select *
            from emp3
            where empno=:empno             
         '''),{'empno':empno})
        #  rows=result.fetchone()
         a=sql.mappings().fetchone()
       
         print('fetchone결과:',a)
           
     except Exception as e :
            print(e)        
    
    
     return templates.TemplateResponse(request,'update.html',{'emp3':a})


    
    
#수정 페이지는 post 방식으로 수행해야하며, 넘는 방식이 잘못된거    
@app.post('/api/update')
def update_emp(emp:Emp3=Form(),
            session:Session=Depends(get_session)):
    print('emp:' ,emp)

    try:
        session.execute(text('''
                  update emp3
                  set 
                  ename=:ename,
                  job=:job,
                  mgr=:mgr,
                  hiredaste=:hiredaste,
                  sal=:sal,
                  comm=:comm,
                  deptno=:deptno
                  where empno=:empno
                              
               '''), {
        'ename': emp.ename,
        'job': emp.job,
        'mgr': emp.mgr,
        'hiredaste': emp.hiredaste,
        'sal': emp.sal,
        'comm': emp.comm,
        'deptno': emp.deptno,
        'empno': emp.empno
    })
        
        session.commit()
# 이걸 commit도 해줘야함
                 
    except Exception as e:
        print('에러 발생 수정요망',e)
        
    
    return RedirectResponse(
        
        url=f'/detail?empno={emp.empno}',
        status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다
    )
    
    
@app.get('/add')
def _add(request:Request):

     print("함수 작동확인?")
     return templates.TemplateResponse(request,'add.html')
 
@app.post('/api/add')
def add(request:Request,emp:Emp3=Form(),
            session:Session=Depends(get_session),
            ):
    print('emp:' ,emp)
    try:
            session.execute(text('''
               insert into emp3(
               empno,   
               ename,
               job,
               mgr,
               hiredaste,
               sal,
               comm,
               deptno)
               values(
                   :empno, :ename, :job, :mgr, :hiredaste, :sal, :comm, :deptno
               )'''),{
              'empno': emp.empno,           
              'ename': emp.ename,
              'job': emp.job,
              'mgr': emp.mgr,
              'hiredaste': emp.hiredaste,
              'sal': emp.sal,
              'comm': emp.comm,
              'deptno':emp.deptno})
            session.commit()
            
    except Exception as e:
       print('에러 발생 수정요망',e)
       session.rollback()
       
    #    어디로 갈지 정하기
    return RedirectResponse(               
            url='/emp/list',
            status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다
           )
    
    
       
# 삭제는 그냥 post로 보내서 지우기만 하면됨
# if문을 이용한 방어 코딩 전략도 세우기

@app.post('/emp/delete')
def _delete_emp(
         emp:Emp3=Form(), # 이거는 EmpDTO를 만들어 둬서 가능한것
         session:Session=Depends(get_session)):
    
        try:
         session.execute(text('''
         delete from emp3
         where empno=:empno                 
        '''),{'empno':emp.empno})
         session.commit()
         
        except Exception as e:
            print('에러 발생',e)
            session.rollback()
            
        return RedirectResponse(               
                    url='/emp/list',
                    status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다
                   )    
           
            

    
    
    


   
# 수정 페이지   
# @app.get('/update')
# def update_emp(
#     request,Request,
#     session:Session=Depends(get_session)
    
# ):
#  return templates.TemplateResponse(request,'update.html',{
#          'todos':todo_list
#      }) 
            
    


    
    # session.commit()
    # session.close() 
    
   
    
   
            


# 서버 키는곳
if __name__ == '__main__':
    print('03_emp:app 파일 직접실행')

    import uvicorn
    uvicorn.run('03_emp:app', port=8000, reload=True,host='0.0.0.0')