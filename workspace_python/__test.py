class Champ:
    def attack(self):
        print('기본 공격')

class Lux(Champ):
    def attack(self):
       super().attack()
       print('데미시아!')
       
class Jax(Champ):
    def defence(self):
        print('방어방어')
        
c1=Lux()                    
c2=Jax()

cList=[c1,c2]

for c in cList:
    c.attack() 
    
'''
부모 car 클래스가 있음
def start(self):
 print('부릉부릉')
def accel(self) 

'''
print('='*20)

class Tank:
    def shoot(self):
        print('탕탕탕!')


class Car(Tank):
    
    
    def Klaxon(self):
        print('빵빵')
    def start(self):
     print('시동을 켭니다')
    
    def accel(self):
     print('속도를 높입니다')
        
class 람보르기니(Car):
    
    
       
    
    
    
     def start(self):
         super().start()
         print('부와아아아아앙!')
         
     def accel(self):
         super().accel()
         print('스아아아아앙')
         
class 티코(Car):
    def accel(self):
        super().accel()
        print('망가짐')
                     
         
         
          
   
    
       
      

c1=람보르기니()
c1.start()
c1.accel()

print('-'*20)
print('티코 달리는중...')
c2=티코()
c2.accel()
c2.Klaxon()
c2.shoot()

from abc import *
# 부모 전용 클래스

class Studentbase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
    
    @abstractmethod
    def go_to_school(self):
       pass
        
class Student(Studentbase):
        def study(self):
            print('공부하기')
        def go_to_school(self):
            print('학교가기')
               
            
a=Student()
a.study()
a.go_to_school()          

# b=Studentbase()
      
                                      