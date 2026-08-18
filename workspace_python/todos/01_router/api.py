from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware

from todo import todo_router
from CRUD import todo_crud

# 위에서 가져온걸 app에다 넣고 실행시킨다

# 크로스 도메인 CORS 해결 코드
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)
 

@app.get("/")
async def welcome() -> dict:
    return {
        "message":"Hello World2"
    }

app.include_router(todo_router)
app.include_router(todo_crud)


@app.get('/ip')
def test(req: Request):
    ip=req.client.host
    print(ip)
    
    return ip



print(1,__name__)

if __name__=='__main__':
    print('api.py 파일 직접실행')
    
    import uvicorn
    uvicorn.run('api:app',port=8000,reload=True)