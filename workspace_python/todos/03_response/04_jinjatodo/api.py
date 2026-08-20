from fastapi import FastAPI,Request
app=FastAPI()

# RedirectResponse-> 이따 사용할것임 
   

@app.get('/jinja')
def step1(id:int=Form(),item:str=Form()):
    # data=requset.query_params
    # item=data.get('item')
    print(id,item)
    return{
        'item':item
    }
    

# 추가
@app.get('/jinja/add')
def step2():
    pass


    