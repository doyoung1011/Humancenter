# for i in range(5):
#     print(i,end=' ')
    
#     print()
# for i in reversed(range(5)):
#   print(i,end=' ')
  
  
  
'''
구구단 출력하기!
'''
# print()
# # number=int(input('숫자를 입력하세요'))
# # print(number)

# for i in range(1,10):
#     print(f'2*{i}= ',2*i)
#     # 출력을 2*1이렇게 변환
    
# for i in range(1,10):
#     print(f'3*{i}= ',3*i)
    
# for i in range(1,10):
#     print(f'4*{i}= ',4*i)
    
    #  반복문에 떄려 넣자아아
    # 바뀌는건 앞의 숫자뿐 
    

for i in range(2,10):
    # 1부터 9까지 반복
     for j in range(1,10):
        #  print(f'{i}*{j} =',i*j)
         
         for k in range(i,i+3):
            print(f'{k}*{j} =',k*j,end=' ')
         print()
         
#    i는 2,5,8
# 

# i=range(2,9,3)
# j=range(1,10)

# for j in range(1,10):
#     print(f'{i}x{j}={i*j}')
        

#  주사위 문제

import random
# print(random.random())
print(random.randint(1,6))
# 랜덤으로 주사위를 던지는 중
count=0
dice=-1

# 주사위 3이 몇번만에 나오는가 
while dice !=3:
  dice=random.randint(1,6)
  count=0 #몇 번 셌는지 체크하는 용도임
  if dice==3:
      print(count)
      
   
   
     
     
'''
반복문 연습
'''
for i in range(5):
    for j in range(5):
        if j<=i:
         print('*',end='')
    print() 
    
    
for i in range(5):
    for j in range(5):
        if i<=j:
         print('*',end='')
    print()
    
    
'''별을 출력하지 않는 부분은 print()로 감싸줘야함'''
print('-'*50)
num=int(input('숫자 아무거나 입력:'))
# 숫자를 하나 입력했을떄 프린트가 되도록 생각
for i in range(num):
    for j in range(num):
        if j<=i:
             print('*',end='')
    print()
            
      
        
    #  print('*',end='')
    
'''
피라미는 왼쪽을 찍어보고,
오른쪽을 찍은 다음에 합치면 될거같음

'''
num1=int(input('숫자 아무거나 입력:'))
# 숫자를 하나 입력했을떄 프린트가 되도록 생각
for i in range(num1):
    for j in range(num1):
        if j<i:
             print('*',end='')
        else:
            print('*',end='')  
            
'''
공백은 점점 줄어드는 구조니까 k를 두게됨
'''

  
                


        
    
    
    
    
 

         


    
      
      

             
      




        
    
   
    
   
    
    
    
    
    

 

