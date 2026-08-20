from fastapi import FastAPI,Request
app=FastAPI()

@app.get('/step1')
def step1(requset:Request):
    data=requset.query_params
    item=data.get('item')
    print(f'item:{item}')
    
    print('너무 복잡하고 정교해서 복붙하기 좀 그런 곳이거덩거덩!')
    
    
@app.get('/step2')
def step2(requset:Request):
    data=requset.query_params
    item=data.get('item')
    print(f'item:{item}일 처리는 끝났구')
    print('step1으로 이동')
    # 1. forward 방식
    step1(requset)

from fastapi.responses import RedirectResponse    
@app.get('/step3')    
def step3(requset:Request):
    print('step3 실행')
    data=requset.query_params
    item=data.get('item')
    print(f'item:{item}일 처리는 끝났구')
    
    print('step1으로 이동')
    # 2. redirect 방식
    return RedirectResponse(
        url='/step1',
        status_code=307 #기본값
    )
    # 303: 다시 올떄 get 방식으로 접속
    # 307: 다시 올 떄 원래 방식 유지
    # 현재는 303 방식 사용할 예정
  
           
    
    

if __name__ == '__main__':
    
 import uvicorn
 uvicorn.run('api:app', port=8000, reload=True,host='0.0.0.0')