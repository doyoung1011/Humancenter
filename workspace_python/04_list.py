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

print(':='*50)
c=[1,5,50,99,45,32,111]
c.sort(reverse=True)

print(c)

c=c[::-1]
print(c)

c.reverse()
print(c)

d=c.pop()
print(c,d)

c.insert(0,100)
c.insert(10,200)

print(c)
c.extend([1,2])
print(c)

a=[1,2,3,4,2]
a.remove(2) #처음 만나는 값을 찾아서 지워버림
print(a)

if 5 in a:
    a.remove(5)


a=[1,2,3,4,2,4]
b=a.index(2)
print(b)

# b=a.index(5000)

c=a.count(4)
print(c)

a.reverse()
print(a)
a.clear()
print(a)

a=[1,2,3]
print(a[len(a):])

a[3:]=[4,5,6]
print(a)

a=[1,2,3,4,5]
b=a
print(b)
b[2]=30
print(b)
print(a)

a=[1,2,3,4,5]
b=a.copy()
b[2]=30
print(b)
print(a)

a=[10,20,30]
for i in a:
    print(i)
    ''' 이번턴의 index, value를 한번에 뽑아줌'''
for index,value in enumerate(a):
    print(index,value)
    
for index,value in enumerate(a,start=100):
    print(index,value) 
    

# a=[7,3,5,8,4]
# # 가장 큰 수 찾기

# # for i in a:
# #     if a[0]>a[1]:
# #         a.append(a[0])
# #         a.remove(a[0])
# #         print(a)
# #         if a[1]>a[2]:
# #             a.append(a[1])
# #             a.remove(a[1])
# #             if a[1]<a[2]:
# #                 a.append(a[2])
# #                 a.remove(a[2])
# #                 print(a)
# #                 if a[2]<a[3]:
# #                     a.append(3)
# #                     a.remove(3)
# #                     print(a)
                
                
                
            
        
    
    
    # elif a[1]>a[2]:
    #     a.append(a[1])
    #     a.remove(a[1])
    # elif a[1]<a[2]:
    #     a.append(a[2])
    #     a.remove(a[2])
    #     print(a)
    #     break
    
   
    # a=[]
    # for i in range(10):
    #        a.append(i)
  
    # a=[i for i in range(10)] 
        
    a=[]
    for i in range(10):
        if i%2==0:
            a.append(i)
    
    a=list( i for i in range(10) if i%2==0)    
    print(a)    
     
a=[1.2,2.5,3.7,4.6,-3.5]
for i,value in enumerate(a):
    a[i]=int(a[i])
print(a)

'''
두번 째 반복되는 것을 하나씩 꺼내서
첫번쨰 함수에 넣고 결과를 배열로 만들어줌

'''

a=map(int,a)
print(a)    

a=[
    [10,20],
    [30,40],
    [50,60]
]   
print(len(a))
print(a[1][0])
    
        

# a.sort()
# print(a[-1])
        
    

# a.sort()
# print(a)

