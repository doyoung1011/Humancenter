# 비어있는 리스트 생성
todo_list=[]

d1={
    'id':1546,
    'item':'item1'
}
#  여기가 crud가 되어있는 곳

# d1을 리스트에 추가합니다.
# Create
todo_list.append(d1)
print(todo_list)

d2={
    'id':24566,
    'item':'item1'
}
todo_list.append(d2)
print(todo_list)

# id가 24566인 것의 딕셔너리 출력
# Read
for i in todo_list:
    print(i.get("id"))
    if i.get('id')== 24566:
        print(i)
        
        
for i in todo_list:
    if i.get('id')== 24566:
        i['item']='아이템2'
print(todo_list)

#   id가 24566인 것의 index를 찾아내고 pop으로 해당 index를 지우기

print('*'*25)

for i in range(len(todo_list)):
    print('i',i)
    if todo_list[i]['id']==24566:
        todo_list.pop(i)
        break
print(todo_list)

# 다른 방법
# 원본을 훼손하지 않는 방법

todo_list=[ todo for todo in todo_list if todo['id']!=24566]
print('-'*40)
print(todo_list)

# 할 일
# crud.py
# todo_list에 CRUD하는 라우터를 설정하고->ok
# api.py를 실행해서 테스트하기

# /crud[GET,POST,PUT,DELETE]


 
   


      