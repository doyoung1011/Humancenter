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


a=list(range(6))

del a[3]
print(a)

a=a+[6]
a.append(8)
print(a)

b=[9,10]
a.append(b)
print(a)

c=[1,5,50,99,45,32,111]
c.sort()
print(c)

c=c[::-1]
print(c)

c.reverse()
print(c)

d=c.pop()
print(c,d)

c.insert(0,100)
c.insert(10,200)


