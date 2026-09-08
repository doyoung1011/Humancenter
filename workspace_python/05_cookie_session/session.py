from fastapi import FastAPI,Cookie,Request,Response
from starlette.middleware.sessions import SessionMiddleware

from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

app=FastAPI()
templates = Jinja2Templates(directory='templates/')

app.mount(
    "/static", #url 경로
    StaticFiles(directory="static"),
    name="static"
)  
app.add_middleware(
    SessionMiddleware,
    secret_key='human1234$'
)

@app.get('/login')
def login(req:Request):
    #세션 저장
    req.session['isLogin']=True
    req.session['id']="admin"
    
@app.get('/mypage')
def mypage(req:Request):
    isLogin=req.session.get('isLogin',None)
    id=req.session.get('id',None)
    if isLogin is None:
        return "로그인이 필요합니다"
    else:
        return f"id:[{id}] 비밀 공간환영합니다"
    
@app.get('/logout')
def logout(req:Request):
    req.session.clear()
    return "로그아웃"
        
@app.get('/')
def home(req:Request):
 return templates.TemplateResponse(req,'main.html')
    


if __name__ == '__main__':
 import uvicorn
 uvicorn.run('session:app', port=8000, reload=True,host='0.0.0.0')