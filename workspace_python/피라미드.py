'''
피라미드 제작기.

1. 나는 어떻게 했는지를 생각하기
빈칸 4개만들기
별표 한개 만들기
엔터 

2. 어려운 문제는 작게 쪼갠닷



'''
# 4개의 빈칸을 만들어야함


# for i in range(5):
#     for j in range(5,-1):
#      print('*',end='')
#      print()



   

# a=int(input('숫자를입력하시오:'))
# for i in range(a+1): #사용자가 입력한거 +1까지 
#     print('_',end='')
#     for j in range(a):    
#         print('*')
#         print('_')

# c = int(input('피라미드 높이: '))

# for a in range(4):
#  for b in range(4 - a - 1):
#     print('_', end='')
#  for b in range(a * 2 + 1):
#     print('*', end='')
#  print()

#피라미드 규칙이해용 코드임
# 규칙을 이해해보자

# 4개의 빈칸을 만들어야함





# 이거를 4번 반복
# print('',end='')
# 4부터 0까지 반복
# print('----*')
# print('---***')
# print('--*****')
# print('-*******')

for i in range(5):
   # 공백부터 찍어야함
    for j in range(5-1-i):
      print('-',end='')
     
    for k in range(2*i+1):
      print('*',end='')
      
    print() 
    
    
   
     
# 공백부터 찍자아

# for i in range(4):
#     for j in range(4):
#      print('-',end='')
#      print()
#      print('*',end='')

# for i in range(4):
#     for j in range(5*2-1):
#      print('-',end="")
#      for k in range()


# 반복 횟수랑 별의 개수를 연관지어서 반복문 수행
