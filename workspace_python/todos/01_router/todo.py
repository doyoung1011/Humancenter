from fastapi import APIRouter,Form,Request
# from fastapi import APIRouter
from model import Todo

todo_router=APIRouter()

todo_list=[]

@todo_router.post('/todo')
async def add_todo(todo:dict)->dict:
    print('todo:',todo)
    todo_list.append(todo)
    return{
        "message": "정상적으로 추가되었습니다."
    }
    
@todo_router.get('/todo')
async def retrieve_todo()->dict:
        return{
            "todos": todo_list
        }
 
 
'''
get 방식일때는 변수명이 HTML에서 사용한 변수명과 동일해야함.
'''
      
@todo_router.get('/todo/param')
async def todoParamGet(id: int ,item:str='')->dict:
    print(id,item)
    return{
        "id":id,
        "item":item
    }
    
  
@todo_router.post('/todo/param')
async def todoParamPost(id: int=Form() ,item:str=Form())->dict:
    print(id,item)
    return{
        "id":id,
        "item":item
    } 
        
@todo_router.get('/todo/param2')
@todo_router.post('/todo/param2')
@todo_router.put('/todo/param2')
@todo_router.delete('/todo/param2')
async def todoParam(req:Request)->dict:
    if req.method=='GET':
        data=req.query_params
    else:
       data=await req.form()
    
    id=data.get('id')
    item=data.get('item')
    print(id,item,req.method)
   
    return{ 
        "id":id,
        "item":item
        
    }    

# 43페이지 실습이라서 todo43
@todo_router.post('/todo43')
def add_todo43(todo:Todo)->dict:
   print(f'todo:{todo}')
   todo_list.append(todo)
   
   return{
       'code':'성공성공성공!'
   }
   
# 주소에 값을 넣을 수도 있다.   
@todo_router.get('/todo/{todo_id}')
async def get_single_todo(todo_id: int) -> dict:
    print(todo_id)
    for todo in todo_list:
        if todo.id==todo_id:
            return{
                'todo':todo
            }  
    return{
        'message':'id없음'
    }
# 잠시 주석 처리함
# from fastapi import Path
# from typing import Annotated        
# @todo_router.get('/todo3/{todo_id}')
# async def get_single_todo3(todo_id): Annotated[int,Path(ge=10)] -> dict:
#     print(todo_id)
#     for todo in todo_list:
#         if todo.id==todo_id:
#             return{
#                 'todo':todo
#             }  
#     return{
#         'message':'id없음'
#     }

# get 방식일 때 즉 ? 뒤에 오는 쿼리스트링
from fastapi import Query

@todo_router.get('/todo4')
def todo4(id:int=Query(gt=0,lt=10000)):
    print(id)    
          

        
print(2,__name__)
if __name__=='__main__':
    print('todo.py 파일 직접실행')