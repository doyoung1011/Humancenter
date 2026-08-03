
class Person:
    
    # 클래스가 생성될 떄 무조건 가장 먼저 실행됨
    # 자동으로 먼저 실행되는 메소드
    def __init__(self):
        print(1)
        self.hello='안녕?'
     
    def greeting(self):
        print(self.hello)
        

        
    def hello(self):
            self.greeting()    
        

             
        
print(0)        
james=Person()
james.greeting()

print(type(james))       

class Person2:
    def __init__(self,name,age):
        print('__init__실행중')
        self.hello='안녕하세요?'
        self.name=name
        self.age=age
        
        
        print(1)
        self.hello='안녕?'
     
    def greeting(self):
        print(f'{self.hello}! 저는 {self.name}이고 나이는 {self.age}입니다')
        
        
class Person3:
    def __init__(self,money):
        print('__init__실행중')
        self.hello='안녕하세요?'
        self.__money=money
        
        
    def pay(self,price):
        self.__money-=price
        print('남은돈: ', self.__money)
        self.__study()
        
    def __study(self):
        print('나혼자 공부중')    
        
             
   
a=Person3(10000)
a.pay(3000)
# a.__study()

# __붙은 변수나 함수는 
# 내부에선느 접근가능하고, 
# 외부로 노출되지 않는다
# 캡슐화,은닉화

     
        
        
        
a=Person2('이름',20)        
a.greeting()
print(a.hello)
print(a.name)    

b=Person2('다른이름',50)
b.greeting()
print(b.name)    

b.addr='천안'
print(b.addr)

# 없는 속성을 만들어서 임시로 사용 가능함.

b.__init__(1,2) #실행이 되긴함...!


