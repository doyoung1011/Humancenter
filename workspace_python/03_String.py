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

a=['a','b','c','d','e']
b='-'.join(a)
'-'.join(a)
a=[1,2,3,4,5]
'-'.join(str(data) for data in a)




print(b)
c=b.split('-')
print(c)

a="Don't Look Back in Anger"
b=a.find('back')
print(b)

c=a.upper()
print(c)

d=a.upper().find('back'.upper())
print(d)

a='    a b   '
print(a.strip())

print('35'.zfill(4))
print('35000'.zfill(4))

a=7
print(f'{a:3}')
print(f'{a:<3}')

a=3.14
print(f'{a:08.3f}')

a=15000
print(f'{a:,}')