class God:
    def MakingWorld(self):
        print('세상은 나만 만들거임')


class Person:
    # def __init__(self):
    #     self.hello='안뇽?'
    def greeting(self):
        print('안녕하세용')
    
class Student(Person):
    def study(self):
        print('열공')
        self.greeting()
        # print((self.hello))
        
class Person2:
    def __init__(self):
        print('Person2 __init__ 실행')
        self.hello='방가'  
        
class Student2(Person2):
     def __init__(self):
            print('Student2 __init__ 실행')
            super().__init__()
            self.schollo='휴먼' 
                
        
class Baby(God):
    def cry(self):
        print('응애!') 

class Student3(Person2):
     def test(self):
         print('테스트중')
         
print('-'*20)
a=Student3()

class Person3:
    def __init__(self,str):
        print('Person3__init__실행')         
        self.hello='방가'  
        self.str=str  
        
class Student4(Person3):
    
    def __init__(self):
        super().__init__(None)
        
class Person5:
    def hi(self):
        print('안녕하시오')

class Student5(Person5):
    def hi(self):
        print('거제에 야호~')       

s5=Student5()
s5.hi()        
        
        
        
print('-'*60)        
s4=Student4()
print(s4.hello)        
print('-'*60) 
         
                
               

        
s1=Student()          
s1.study()      
s1.greeting()

s2=Student2()
print(s2.hello)
# print(s1.hello)      

s2=Baby()
s2.MakingWorld()


print('-'*40)


