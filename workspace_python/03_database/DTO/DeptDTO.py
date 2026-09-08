from sqlmodel import SQLModel,Field
from typing import Optional

from DTO.EmpDTO import Emp3
from DTO.DeptDTO import DEPT3

class DEPT3(SQLModel,table=True):
    deptno:int=Field(primary_key=True)
    dname=str
    loc:str
    
    mgr=Optional[int]=None
    hiredate:str
    sal:float
    comm:Optional[float]=None
    
    deptno:int= Field(
        foreign_key='dept3.deptno'
    )
 
 
 
    
