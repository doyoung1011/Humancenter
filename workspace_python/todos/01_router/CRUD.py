from fastapi import APIRouter,Form,Request
# from fastapi import APIRouter
from model import Todo



# import 완료

# API 주소를 붙일곳
todo_crud=APIRouter()
# CRUD할 데이터저장
todo_list=[]


d1={
    'id':1546,
    'item':'item1'
}
todo_list.append(d1)

# pydantic으로 구현하는중..
# Create 구현
@todo_crud.post('/crud')
async def todo_Create(todo:Todo)->dict:
   print(todo)
   
   todo_list.append(todo)
   return{
        "todos": todo_list
   }

# Read 구현하기!!   
@todo_crud.get('/crud')
async def todo_Read()->dict:
    print(todo_list)
    return{
           "todos": todo_list
      }
# Update 구현하기 
       


# 할 일
# crud.py
# todo_list에 CRUD하는 라우터를 설장하고
# api.py를 실행해서 테스트하기

# /crud[GET,POST,PUT,DELETE] 이걸 한번에 하는 코드로 제작해보기


# 메소드를 여기서 구현하겠다는 의미임
# crud순서대로 구현시작.


print(2,__name__)

if __name__=='__main__':
    print('CRUD.py 파일 직접실행')