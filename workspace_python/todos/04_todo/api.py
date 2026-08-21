from fastapi import FastAPI, Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse    
from todo import Todo

app = FastAPI()
templates = Jinja2Templates(directory='templates')
# 임시 테스트 2026-08-21
# 생성을 아직 안 만들어서 
todo_list=[]
todo=Todo(id=999,item='test')
todo.item='test'
todo_list.append(todo)
todo_list.append(todo)
todo_list.append(todo)

# STEP 1: 사용자가 첨에 볼거
@app.get('/todo')
def list(request:Request):
    print('/todo 전체목록조회 가능여부  ')

    return templates.TemplateResponse(request,'todo.html',{
        'todos':todo_list
    })

@app.get('/add')
def add(request:Request):
    print('/todo/c 추가가능여부  ')

    return templates.TemplateResponse(request,'add.html')
    
@app.get('/api.add')
def apiAdd(todo:Todo):
    print('/api/add')
    print('todo',todo)
    
    todo_list.append(todo)
    return RedirectResponse(
        url='/lsit',
        status_code=303
    )
    
    
 
@app.get('/detail/{id}')
def detail(request:Request,id:int):
    # 반복문 찾아서 돌려야뎌
    print('detail 실행')

    return templates.TemplateResponse(request,'todo.html',{
        'todos':todo_list
    }) 
    
    for todo in todo_list:
        if todo.id == id:
            print(todo)
            # return todo
            result = todo   
    # 여기는 아직 타이핑 못함 이따 수행
    
@app.get('/update')
def details(request:Request,id:int):
       
    



 if __name__ == '__main__':
    print('api.py 파일 직접실행')

    import uvicorn
    uvicorn.run('api:app', port=8000, reload=True,host='0.0.0.0')
    