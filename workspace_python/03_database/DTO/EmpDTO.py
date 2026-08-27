from sqlmodel import SQLModel,Field
from typing import Optional
from pydantic import BaseModel, model_validator

# emp3를 조회할때 필요한 파일
class Emp3(SQLModel,table=True):
    # 없으면 클래스명이 테이블명이 된다.
    # __tablename__='emp'
    
    # empno:int=Field(primary_key=True)
    empno: int| None=Field(
        default=None,
        primary_key=True
        ) # auto_increment
    ename:str
    job:str
    # mgr:int | None=None # int가 null이면 none으로 처리해라
    mgr:Optional[int]=None
    hiredaste:str
    sal:float
    # comm:float | None=None
    comm:Optional[int]=None
    deptno: int
    


'''
모든 변수 검증하는곳
'''

# @model_validator(model='before')
# @classmethod

