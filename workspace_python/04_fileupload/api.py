
from fastapi import FastAPI, Form, UploadFile, File,HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import shutil
from datetime import datetime
import uuid


app=FastAPI()

dir=Path('uploads')
dir.mkdir(exist_ok=True)

@app.get('/upload')
def _upload(
    # None: 필수 아님
):
    print('hello world')
    

@app.post('/upload')
def upload(
    # title=Form(...), # 명시적으로 필수 값 표시
    title=Form(), #...은 생략 가능함
    content=Form(None),
    file1: UploadFile=File(),
    file2: list[UploadFile]=File() #파일 여러개
):
    print('title:',title)
    print('content:',content)
    # print('file1:',file1)
    
    print('file.SIZE', file1.size)
    print('file.SIZE', file1.filename)
    
    filename_orig=file1.filename
    # 새로운 파일명
    # print('now',datetime.now())
    # t=datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    # filename_safe=f'{t}_{filename_orig}'
    print('uuid.uuid:',uuid.uuid4())
    filename_safe=f'{uuid.uuid4().hex}_{filename_orig}'
    
    # 경로 합치기
    # '/' : Path가 지정한 결합 연산자라서 쓸 수 있음
    target_path= dir / filename_safe
    '''
    w: 쓰기
    b: binary 즉 파일 그 자체
    '''
    with target_path.open('wb') as buffer:
# buffer.write를 써도 되지만 큰 파일의 경우 메모리 등의 문제 존재
# hutil.copyfileobj 는 조금씩 쪼개서 안전하고 효율적으로 저장할 수 있다.
        shutil.copyfileobj(file1.file, buffer)
        
        
# file2처리 파트
    for f in file2:
        print(f.filename)

@app.get('/download')
def download(file_name):
 file_path =dir/file_name    
 
 if not file_path.exists():
     raise HTTPException(
         status_code=404,
         detail='파일을 찾을 수 없습니다'
     )
 
 return FileResponse(
      path=file_path,
      filename=file_name,
      # filename='a.txt',
      media_type='application/octet-stream')     
 
        
    
    
   


if __name__ == '__main__':
    
 import uvicorn
 uvicorn.run('api:app', port=8000, reload=True,host='0.0.0.0')
