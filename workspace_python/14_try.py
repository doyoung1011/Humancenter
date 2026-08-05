
def div(x,y):
    result=0
    if y!=0:
        result =x / y
    else:
        print("두 번쨰 숫자는 0불가" )
    return result    
       
        
def div2(x,y):
    result=0
    try:
        result= x/y
    except:
        print('예외 발생함')    
   
    return result

def div3(x,y):
    result=0
    try:
        result= x/y
    except TypeError:
        print('숫자만 넣어주세요.')
    except ZeroDivisionError:
        print('0으로 나눌수 없습니다.')        
   
    return result

def div4(x,y):
    result=0
    try:
        result= x/y
    except TypeError as e:
        print('숫자만 넣어주세요.',e)
    except ZeroDivisionError as e:
        print('0으로 나눌수 없습니다.',e)        
   
    return result

def div5(x,y):
    result=0
    try:
        result= x/y
    except Exception as e:
        print('예외 발생',e)
        
   
    return result

def div6(x,y):
    result=0
    try:
        result= x/y
    except Exception as e:
        print('예외 발생',e)
    else:
        print('문제 없었다')    
    return result

def div7(x,y):
    result=0
    try:
        result= x/y
       
        return result
    except Exception as e:
        print('예외 발생',e)
    else:
        print('문제 없었다')
    finally:
        print('무조건 실행')        
    return result
'''
  finally는 무조건 실행되며 return을 해도 무조건 실행됨 
'''


a=div(7,2)
print(a)

a=div2(7,0)
print(a)

print('-'*50)
div3(7,0)
div3(7,'a')
print('-'*50)

div4(7,0)
div4(7,'0')

print('-'*50)

div5(7,0)
div5(7,'0')

print('-'*50)

div6(7,0)
div6(7,2)
print('-'*50)

div7(7,0)
div7(7,2)
print('-'*50)
'''
무중단 프로그래밍의 원리

'''
print('-'*50)

# raise Exception('404 Not Found')

def loginCheck(id,pw):
    if id=='admin' and pw =='1234':
        print('로그인 성공')
        return 0
    
    elif id=='':
        print('id를 입력해주세요')
        return 1
        
def login():
    id='admin'
    pw='1234'
    result=loginCheck(id,pw)
    
    if result==0:
        print('메인 페이지로 이동')
    elif result==1:
        print('아이디를 입력해주세요') 
        
def loginCheck2(id,pw):
    if id=='admin' and pw =='1234':
        print('로그인 성공')
        return 0
    
    elif id=='':
        print('id를 입력해주세요')
        raise Exception('code:1')
    
    
def login2():
    id=''
    pw='1234'
    result=loginCheck(id,pw)
    
    if result==0:
        print('메인 페이지로 이동')
    elif result==1:
        print('아이디를 입력해주세요')             
        
        
login()
login2()           

import traceback
try:
    a=3/0
except  Exception as e:
    print(e)
    a=traceback.format_exc()
    print('-'*30)
    print(a)                    