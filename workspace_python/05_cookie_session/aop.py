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


EXCLUDE_PATH = [
    '/login'
   
]


@app.middleware('http')
async def login_chk(request: Request, call_next):

    # 사용자가 어떤 경로로 들어왔는지 확인
    url_path = request.url.path

    # 로그인 검사 제외 경로가 아닐 때만 검사
    if url_path  in EXCLUDE_PATH or  url_path.startswith('/static'):
        # 제외 경로거나 
        # /static으로 시작한다면
        # 그냥 통과
            return await call_next(request)
    else:

        # 세션에 로그인 정보가 없으면 로그인 페이지로 이동
        isLogin = request.session.get('isLogin', None)

        if isLogin is None:
            return RedirectResponse(
                url='/login',
                status_code=302
            )
        else:
            return await call_next(request)    

    # 로그인 상태이거나 제외 경로면 원래 요청 계속 진행



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
 uvicorn.run('aop:app', port=8000, reload=True,host='0.0.0.0')