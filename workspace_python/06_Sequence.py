a=[0,10,20,30,40]
print(20 in a)
print(200 in a)
print(not(200 in a))
print( 200 not in a)

a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

# 문자열 + 문자열도 가능함

a='hello'
b='world'
c=a+b
print(c)

# c=a+3
c=a+str(3)
print(c)

print('-' *10)

print(len(a))

hello='안녕하세요'
b=hello.encode('utf-8')
print(len(b))

a=[1,2,3,4]
print(a[-2])

# print(a[100])
# 범위가 벗어났으므로 에러발생


a=(1,2,3)
print(a[0])
# a[0] 튜플의 값은 바꿀수 없오

a=[0,1,2,3,4,5,6,7,8,9]
print(a[1:4])
# 1부터 4앞까지
print(a[4:100])
# 범위를 벗어나도 에러 X

print(a[1:9:2])

print( a[:7])
print(a[5:])
print(a[:])

print(a[7:3:-1])

a='hello'
print(a[::-1])

