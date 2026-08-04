
class Person:
    
    # 클래스명은 대문자로 시작되는게 국룰임
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
        # print('__init__실행중')
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

# class Knotted:
#     # 입구에 있다.
#     # 노티드라는 클래스가 공통으로 가지고 있는 것
#     brand='노티드-디저트 맛집!'
    
#     def __init__(self,name,address):
#         # self.brand='노티드-디저트 맛집!'
#         self.name=name
#         self.address=address
#     def info(self):
#         print(self.name)    
        
# print('-'*30)        
# k1=Knotted('천안점','천안')        
# k2=Knotted('부산점','부산')        
# # k3=Knotted('아산점','아산')        
   
# print(k1.name,k1.brand)
# print(k2.name,k2.brand)
# print('-'*30)

# k1=Knotted('천안점','천안')  
# k2=Knotted('아산점','아산')  

# print()
# print('-'*30)
# print('이게 좀더 효율적인 코드임')
# print('='*30)

# # 클래스를 읽기만 하면 바로 메모리로 올라감  
# print(k1.name,Knotted.brand)
# print(k2.name,Knotted.brand)          
# print('='*30)

'''
 @로 붙은 애들은 데코레이터


'''

class Calc:
    PI=3.141592
    @staticmethod
    def add(x,y):
        return x+y
    @staticmethod
    def div(x,y):
            return x/y
        
print(Calc.add(1,2))    
print(Calc.div(1,2)*Calc.PI)

class Person4:
    count=0
    
    def __init__(self):
        Person4.count+=1
        
    @classmethod
    def print_count(cls):
        print(f'{cls.count}명 생성 됨')
        
p1=Person4()            
p2=Person4()            
p3=Person4()            
p4=Person4()            
Person4.print_count()


'''
문제 1
멜론 차트 관리 시스템
모든 곳을 리스트로 관리
한 곡에 해당하는 클래스부터 만들자
-제목,가수명,앨범명,가사

두 곡 이상의 정보를 저장
각 곡의 '제목-가수명'을 출력함

문제 2
휴먼잡스 계정 관리 시스템
내 계정에는 id,pw,주소가 있다
모두 접근 제한된 private 변수입니다.

메소드를 이용해서 주소를 변경하거나
주소를 return하는 메소드를 만들기

문제 3
디저트 카페 창업을 위한 클래스
 -상호,자본금이 필수 요소
노티드를 2군데 창업할 것이다
하나를 창업할 때 필수 요소를 꼭 넣어야 생성되도록 만드시오.
(__init__로 받으라는 의미) 

'''

print('-'*30)
print('문제 1번')
print('-'*30)


class Melon:
    def __init__(self,title,singer,album,lyric):
        self.title=title
        self.singer=singer
        self.album=album
        self.lyric=lyric
    

song_list=[]     #노래 목록 생성
song1=Melon('LOVE ATTACK','리센느','SCENEDROME','Like me, like me 아주 눈이 부신너를 숨김없이 보여줘...')
song2=Melon('캐치 캐치','최예나','LOVE CATCHER','심장이 up, down, down 또 up, down 사랑의 화살을 당겨 봐')
    
song_list.append(song1)
song_list.append(song2)

for list in song_list:
   print(f'{list.title}-{list.singer}')
   
print('-'*30)   
print('문제 2번')
print('-'*30)   
# 비공개 속성은 클래스안에서만 사용가능함을 기억하고 코드작성하기.


class HumanJobs: 
    # 비공개 속성 생성하기
    # 언더바를 두개 붙히면 접근 제한됨
    def __init__(self,id,pw,addr):
        self.__id=id
        self.__pw=pw
        self.__addr=addr
      
        
    def getID(self):
        return self.__id
    
    def getPW(self):
        return self.__pw
    
    def changeAdd(self,addr):
        self.__addr=addr
    
    def getAdd(self):
        return self.__addr
    #테스트 진행
test=HumanJobs('1234','1','아산')
test.changeAdd('부산')
print(test.getID())
print(test.getAdd())



'''
안에서 건들고 그걸 변수에 담아서 출력하는 식으로 접근해야함.

'''

# test.getAdd()     
# test.changeAdd()     



    
print('문제3번')
print('-'*30)  

# 문제 3번의 경우 전달인자를 무조건 2개를 받는 구조 



class Knotted2:
    def __init__(self,상호,자본금):
        self.상호=상호
        self.자보금=자본금
        
k1=Knotted2('북한점',20000)
   

# 문제 2번 강사님 버전

# class Melon2:
#     def __init__(self):
#         self.songList=[]
        
#     def appendSong(self,song):
#         self.songList.append(song)    

# m=Melon()

   
   
        
        
        
        
        
 
    

# class HumanJobs:
#     id='1234'
#     pw='1234'
#     def management(id,pw,address):
#         print(id,pw,address)
        
#     def management1(id,pw,address):
#         print(id,pw,address)
            
           