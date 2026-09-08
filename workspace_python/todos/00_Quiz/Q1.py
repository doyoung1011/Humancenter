from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 위에가 서버 키는거...

# 서버를 켜서 hello world부터 찍자
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get("/q1") 
def html(dan: int):
    print('dan', dan)
    # x=int(dan)
    for i in range(10):
        print(f'{dan}X{i}={dan*i}')    
        # 구구단 제작하기
        
@app.get("/hap") 
def hap(x: int, y:int=0):
    print(x,y)
    print(x+y)
    
# 유비콘을 직접안키고 파이썬으로 실행시키기 위한 코드
if __name__=='__main__':
    print('Q1.py 파일 직접실행')
    
    import uvicorn
    uvicorn.run('Q1:app',port=8000,reload=True)    
