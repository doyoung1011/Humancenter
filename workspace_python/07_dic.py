#딕셔너리의 선언
a={}
a=dict()
print(type(a))

b={
    '이름': '호랑이 심장',
    '직업': '전사',
    '스킬': {
        '공격': '불주먹!',
        '방어': '차단',
        'javascript':'중'
        
    }
    
    
}
print(b)
c=dict(a=10,b=20)


print(b['이름'])
print(b.get('이름'))
print(b.get('이름2')) #없으면 None
print(b.get('이름2','이름없음')) # 없으면 2번째 값으로 대체

print(b['스킬']['공격'])

print(b.get('스킬').get('공격'))
print(b.get('스킬2',{}).get('공격','0'))

b['직업']='도적'
print(b)


b['직업2']='도적2'
print(b)
#없으면 key 만들어줌

print('스킬' in b)
print('공격' in b['스킬'])
print('공격' not in b['스킬'])

print(len(b)) #key의 개수

e=b.keys()
print(e)
#리스트로 바꿔서 돌려줌...!
f=b.values()
print(f)
print(list(f)[0])

g=b.items()
print(g)

a='hello'
print(list(a))
print(set(a))
#set은 중복을 제거함
# 순서 보장 X
