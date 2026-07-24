a=[]
b=list() #리스트 선언방법
print(type(a))
print(type(b))

a=[1,2,3]
print(a)

# range
# 전달인자 2개: 0~바로 앞까지
c=range(10)
print(c)
print(list(c))

d=range(5,12)
print(list(d))

e=range(12,5)
print(list(e)) # 빈 배열 나옴

f=range(-4,10,2)
print(list(f))
#전달인자 3개: 첫 번째 부터, 두 번쨰 바로 앞까지 나옴 
