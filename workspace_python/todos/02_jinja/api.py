from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.get('/hello')
def hello(request: Request):
    print('/hello 실행')

    return templates.TemplateResponse(request,'home.html',{
        'ip':request.client.host,
        'msg':'hi'
    })
    
@app.get('/youtube')
def youtube(request: Request):
    print('/youtube 실행')

    return templates.TemplateResponse(request,'youtube.html',{
        'like': 3,
        'star':4,
        'bookmark':['동영상1','동영상2','동영상3','동영상4','동영상5']
       
    })
    
def price(value):
    # value=1000
    print(f'{value:,}')
    return f'{value:,}'

templates.env.filters['price']=price
#날짜 포멧

from datetime import datetime
def format_data(value,format='%Y-%m-%D %H:%M:%S'):
    v=datetime.fromisoformat(value)
    return v.strftime(format)
templates.env.filters['format_data']=format_data 

def n2br(value):
    from markupsafe import Markup #innerHTML로 만들어 주는 모듈임
    return Markup(value.replace('\n','<br>'))
templates.env.filters['n2br']=n2br
          
      

if __name__ == '__main__':
    print('api.py 파일 직접실행')

    import uvicorn
    uvicorn.run('api:app', port=8000, reload=True,host='0.0.0.0')