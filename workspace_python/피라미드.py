'''
피라미드 제작기.

1. 나는 어떻게 했는지를 생각하기
빈칸 4개만들기
별표 한개 만들기
엔터 

2. 어려운 문제는 작게 쪼갠닷



'''
# 4개의 빈칸을 만들어야함

# 이거를 4번 반복
# print('',end='')
# 4부터 0까지 반복
# print('_____*')
# print('____**')
# print('___***')
# print('__****')
# print('_*****')

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

# for a in range(c):
#  for b in range(c - a - 1):
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
# print('____*')
# print('___**')
# print('__***')
# print('_ft****')
# print('*****')

# 피라미는 이런식으로 구성됨

# 공백이 밑으로 갈수록 줄어듬

# 5번 반복이라고 가정시


# 공백=5-별 개수
#별 갯수=5-공백


for i in range(1):
    for j in range(0):
     print('_',end="")
     print('*')
    
