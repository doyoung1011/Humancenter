from sqlmodel import SQLModel, Field

class Res_c_day_bridge (SQLModel, Table=True):
    res_code : int = Field(
        primary_key=True,
        foreign_key='Restaurant.res_code'
    )
    c_code : int = Field(
        primary_key=True,
        foreign_key='Closed_days.c_dode'
    )