'''
문제1
numbers = [3, 7, 10, 15, 22, 8, 13]
문제1-1 : 짝수만 따로 리스트로 만들어서 출력
문제1-2 : 홀수의 합

문제 2
cart = {
    '사과': {
        '가격': 1000,
        '개수': 3
    },
    '바나나': {
        '가격': 2000,
        '개수': 4
    },
    '복숭아': {
        '가격': 1500,
        '개수': 2
    },
    '키위': {
        '가격': 2200,
        '개수': 5
    }
}
다 샀을 때 가격은?

문제3
UP/DOWN 게임 만들기
단, 맞추면 몇번째에 맞췄는지도 출력

문제4
users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd"
}
이런 경우 
id/pw를 입력 받거나 변수에 넣어두고
id/pw가 맞는지 틀리는지 판단해서
"아이디가 틀립니다", "비번이 틀립니다", "로그인 성공"


문제5
랜덤 투표 시스템
한번에 a, b, c 대상에 랜덤으로 투표
문제5-1 : 100번의 투표 결과를 출력하시오
문제5-2 : 그 중 가장 득표 많은 사람의 이름과 득표 수 출력




'''

#  문제1
# numbers = [3, 7, 10, 15, 22, 8, 13]
# 문제1-1 : 짝수만 따로 리스트로 만들어서 출력
# 문제1-2 : 홀수의 합

numbers = [3, 7, 10, 15, 22, 8, 13]
even_list=[] # 짝수를 저장할 리스트

for i in range(len(numbers)):
  if numbers[i]%2==0:
      even_list.append(numbers[i])
     
print(even_list) # 짝수리스트 


numbers = [3, 7, 10, 15, 22, 8, 13]
odd_list=[]
for i in range(len(numbers)):
    if numbers[i]%2==1:
        odd_list.append(numbers[i])

print(odd_list)        

sum(odd_list)
print(sum(odd_list))        
        
        
'''
 문제 2
cart = {
    '사과': {
        '가격': 1000,
        '개수': 3
    },
    '바나나': {
        '가격': 2000,
        '개수': 4
    },
    '복숭아': {
        '가격': 1500,
        '개수': 2
    },
    '키위': {
        '가격': 2200,
        '개수': 5
    }
}
다 샀을 때 가격은?
 
 
'''
cart = {
    '사과': {
        '가격': 1000,
        '개수': 3
    },
    '바나나': {
        '가격': 2000,
        '개수': 4
    },
    '복숭아': {
        '가격': 1500,
        '개수': 2
    },
    '키위': {
        '가격': 2200,
        '개수': 5
    }
}


# total=0 #지금까지의 총합
# price=0
# counts=0
# # for key,value in cart.items():
#     # print(key,value)
#     price=value['가격'] #개별 가격
#     counts=value['개수'] #개별갯수
    

#     total+=price*counts
    


# print(total)
# # print(counts)
a=0
for i in cart.keys():
    a+=cart[i]['가격']*cart[i]['개수']
    
print(a)    
    
    


 
 
 


