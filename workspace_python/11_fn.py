def hello():
    print("Hello, world!")

hello()

def add(a,b):
    # __doc__
    # 함수 첫줄의 주석 글씨를 출력해줌
    "a+b를 출력하는 함수입니다"
    print(a+b)
add(1,3)
print(add.__doc__)

def add2(a,b):
    return a+b
result = add2(1,5)
print(result)

def 아낌없이주는함수():
    return 100

def not_ten(a):
    if a==10:
        return
    print(a)
b=not_ten(10)    
print(b)

def add_sub(a,b):
    x=a+b
    y=a-b
    return x,y
# return x,y는 return (x,y)와 같음,즉 튜플임
c=add_sub(1,2)
print(type(c),c)

# x=add_sub(1,2,3)

def prit_numbers(a,b,c):
    print(a)
    print(b)
    print(c)
prit_numbers(10,20,30)  
a=[1,2,3]
print(*a)
prit_numbers(*a)  

def print_numbers2(*a):
    print(type(a),a)
    
print_numbers2(1)    
print_numbers2(1,2,3,4)    

def print_numbers3(c,*a):
    print(c)
    for b in a:
        print(b)
        
def minus(x,y):
    print(x-y)
    
minus(5,2)
minus(y=5,x=2)         

x={
    'name':'유도영',
    'age':'26'
}   
def info(age,name):
    print(age,name)
info(*x)    #딧셔너리의 경우는 *는 key만 추출. 이는 .keys()와 같음
info(**x) #key=value,key

def info2(**a):
    for k,v in a.items():
        print(k,v)
info(**x)        

def info3(name,age,addr='비공개'):
    print(name,age,addr)
    
info3(1,2,3)
info3(1,2)

def local_var():
    a2=10
    # if a2>3:
    #     print(a2)
    #     b2=5
    # print(b2)
# local_var(a2) #a2는 local_val의 지역변수라서 현 시점엔 현 시점에 없음

def ref(a):
    a.append(4)

b=[1,2,3]
ref(b)
print(b)               

def fn1(a):
    return a+10
def fn2(a):
    return a*10
c=10
b=fn1(c) #20이 된상황
d=fn2(b)
print(20)
print(d)

e=fn2(fn1(c))
print(e)
# 이를 통해서 함수에 함수를 넣을 수 있다는 것을 알 수 있음

print(fn1)

def ten(x):
    return x+10

ten2=lambda x: x+10
print(ten2(5))

a=['1','2']
b=[int(a[0]),int(a[1])]
c=list(map(int,a))
print(a,b,c)

d=list(map(ten2,c))
print(d)

e=list(map(lambda x:x+10,c))
print(e)

sqr=lambda x:x**2
sum=lambda x,y:x+y
print(sqr(3))
print(sum(3,5))

info=[{
    'name':'이름',
    'age':25
},
      {
    'name':'이름2',
    'age':23
},
      {
    'name':'이름3',
    'age':28
}]
# 함수로 출력
# 나이만 출력
def print_age(info):
    for p in info:
        print(p['age']) 
print_age(info)        
# info를 전달인자로 받음

print_age2=lambda info:[p['age'] for p in info]

x=10 #전역 변수,global 변수
def foo():
    x=20
    print('foo안에서 x',x)
foo()    
print('foo밖에서 x',x)    

def foo2():
    # x=20
    print('foo2안에서 x',x) #전역 변수 읽기는 됨.
foo2()    
print('foo2밖에서 x',x)    

def foo3():
    global x
    x=20
foo3()
print('foo3 이후의 x',x)    

#함수 안에서 변수 우선 순위
'''
    1. 먼저 지역 변수 찾기
    2. 없으면 전역 변수 찾기
    3. 없으면 에러

'''
x=10

def test(z):
    return z+2
x=test(x)

def test2():
    global x
    x=x+2

x=10
y=20
def test3():
    global x,y
    x=11
    y=12
    
def A():
    x=10
    y=20
    def B():
        x=30
        def C():
            nonlocal x,y
            print(x)
            print(y)
            
        C()
   
    B()
A()        


# pos=10
# def key_rihgt(step):
#     return pos+step
# pos=key_rihgt(4)

# key_rihgt(key_rihgt(4))    