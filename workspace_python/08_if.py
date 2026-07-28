a=10
b=5
print(3<a<20)

if True :
    print(1)
#  print(2)
    print(3)
    if True :
        print(4)
        
if True:
    pass
else:
    pass

if 1:
    print('참')    
    
    '''
    파이썬에서 False란?
    False,None,0,0.0, 빈 컨테이너(비어있는 문자열,리스트,튜플)
    
    
    
    '''
    a=[]
    if a:
        print('참')
    else:
        print('거짓')
        
        # 174p 문제 14.7
# score1=int(input('국어점수입력:'))
# score2=int(input('영어점수입력:'))
# score3=int(input('수학점수입력:'))
# score4=int(input('과학점수입력:'))
# avg=(score1+score2+score3+score4)/4
# if(avg>=80):
#     print('합격!')
# else:
#     print('불합격')
    

# score=input('점수 4개 입력, 띄워쓰기로 구분: ')
# print(score, score.split())
# scores=score.split(' ')
# sum=int(scores[0])+int(scores[1])+int(scores[2])+int(scores[3])
# avg=sum/len(scores)

# if(0<=int(scores[0])<=100) and (0<=int(scores[1])<=100) and (0<=int(scores[2])<=100) and (0<=int(scores[3])<=100):

#  if avg>=80:
#     print('합격!')
#  else:
#     print('불합격 ㅠㅠ')  
# else:
#     print('잘못된 입력')  
    

'''
176페이지

'''
btn=int(input('메뉴를 고르시오!'))

if btn==1:
    print('콜라')
elif btn==2:
    print('사이다')
elif btn==3:
    print('퐌타')
else:
    print('잘 골라라 뒤진다')        

    