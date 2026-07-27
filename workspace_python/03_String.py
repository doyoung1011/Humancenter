a='hello'
b="world"

c='''
여기에 넣을 수 있다
'''
'''
여러줄 주석으로 사용됨
'''

b=32.5
c="지금 온도는"+str(b)+"입니다"
print(c)

d=f"지금 온도는 {b}도 입니다"
print(d)

e="지금 온도는 {0}도 입니다 ".format(b)

f=f'''
<div>
    지금 온도는 {b}도
</div>

'''

print(f)

g='지금 온도는 %d도 입니다' %b
print(g)

h='지금 온도는 %f도 입니다' %b
print(h)

i='_hello'
print(len(i))
print(i.count('l'))
print(i.find('l'))

print(i.rfind('l'))
print(i.replace('l','v')) #전부다 바꿔줌

j='그럼 저기서 하나만 바꾸고 싶으면요?'
k=j.split()
print(k)

m=[1,2,3]
a,b,c=m

