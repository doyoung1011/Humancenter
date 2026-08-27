
import pymysql
from fastapi import FastAPI,Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

app=FastAPI()
templates = Jinja2Templates(directory='templates/')  

def get_connect():
    conn=pymysql.connect(
        host='127.0.0.1',
        port=3306,
        database='human',
        user='root',
        password='human123$',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    return conn
# 20번만 조회
def emp_list_deptno20():
    connect = get_connect()

    try:
        with connect.cursor() as cursor:

            sql = '''
                select * from emp
                where deptno = %s
            '''

            cursor.execute(sql, (20,))

            emp_list = cursor.fetchall()
            print(emp_list)

    except Exception as e:
        print(e)

    finally:
        connect.close()     

@app.get('/emp/deptno')        
def emp_list_deptno(deptno:int,request:Request):
    connect=get_connect()
    
    emp_list=[]
    try:
            with connect.cursor() as cursor:
    
                sql = '''
                    select * from emp
                    where deptno = %s
                '''
    
                cursor.execute(sql, (deptno,))
    
                emp_list = cursor.fetchall()
                print(emp_list)
    
    except Exception as e:
            print(e)
    finally:
        connect.close()
        
    return templates.TemplateResponse(request,'list.html',{
        'emp_list':emp_list
    })          
           
            
    
    
    
       



    
if __name__ == '__main__':
    print('api.py 파일 직접실행')

    import uvicorn
    uvicorn.run('api:app', port=8000, reload=True,host='0.0.0.0')