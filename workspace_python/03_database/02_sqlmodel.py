from fastapi import Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from sqlmodel import create_engine,Session,SQLModel
from fastapi import FastAPI,Depends

from sqlalchemy import text

from DTO.EmpDTO import Emp3 #이를 함으로써 create table을 수행가능함

app=FastAPI()
templates = Jinja2Templates(directory='templates/')  
# Session

DATABASE_URL='mysql+pymysql://root:human123$@127.0.0.1:3306/human'
engine=create_engine(DATABASE_URL,echo=True)
# engine=create_engine(
#     DATABASE_URL,
#     echo=True,
#     execution_options={'isolation_level':'AUTOCOMMIT'}
#     )
# 엔진을 가지고 접속할 준비가 됨

def get_session():
    with Session(engine) as session:
        yield session
        session.commit()

@app.on_event('startup')
def on_startup():
    SQLModel.metadata.create_all(engine)
        
@app.get('/emp/deptno')
def emp_list_deptno(
    request:Request,
    deptno:int,
    session:Session=Depends(get_session)
    
):
    emp2=[]
    try:
        # text: sql문을 실행하기 전에 미리 컴파일 해둔다.
        sql=text('''            
            select *
            from emp3
            where deptno=:deptno     
        ''')
        result=session.execute(sql,{'deptno':deptno})
        emp2=result.mappings().fetchall()
        print(emp2)
        
        
    except Exception as e:
        print(e)
   
    return templates.TemplateResponse(request,'list.html',{
            'emp2':emp2
        }) 
    
@app.get('/emp/update/sal')
def update_sal(
    per:int,
    session:Session=Depends(get_session)
):
    upsal=1+(per/100)
    print('upsal',upsal)
    
    
    
    sql=text('''
        update emp3 
        set sal=sal* :upsal
        where deptno=30
     ''')
    result=session.execute(sql,{'upsal':upsal})
    # 이 코드 참고해서 성공시킴
    # session.commit()
    
    print('실행 결과로 영향을 받은 row 수',result.rowcount)
    
@app.get('/emp/update/sal')
def update_sal(
    per:int,
    session:Session=Depends(get_session)
):
    upsal=1+(per/100)
    print('upsal',upsal)
    
    try:
    
     sql=text('''
        update emp3 
        set sal=sal* :upsal
        where deptno=30
     ''')
     sql=session.execute(sql,{'upsal':upsal})
     # session.commit()
    except Exception as e:
     print('errrrr',e)
     session.rollback() 
    
   
            
        
           
            



# def emp_list_deptno20(
#     session:Session=Depends(get_session)
# ):
#     try:
        
#         # with Session(engine) as session:
            
      
       
#     except Exception as e:
#         print (e)
        
if __name__ == '__main__':
    print('02_sqlmodel:app 파일 직접실행')

    import uvicorn
    uvicorn.run('02_sqlmodel:app', port=8000, reload=True,host='0.0.0.0')