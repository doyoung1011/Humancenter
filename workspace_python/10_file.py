# w는 수정 가능
file=open('hello.text','w')
file.write('eng\n123\n한글테스트')
file.flush()  #버퍼가 꽉 차지 않아도 내보내기
              #즉시 반영 
file.close()

# r은 읽기 전용
# 
file=open('hello2.text','w',encoding='utf-8')
file.write('eng\n123\n한글테스트')
file.close()

file=open('hello.text','r')
s=file.read()
file.close()
print(s)



file=open('hello2.text','r',encoding='utf-8')
s=file.read()
file.close()
print(s)

print('-'*20)
file=open('hello.text','r')
s=file.read(10)
file.close()
print(s)

print('-'*20)
file=open('hello.text','r',buffering=1)
s=file.read(10)
file.close()
print(s)

print('-'*20)
text=''
file=open('hello.text','r')
while True:
    chunk=file.read(2)
    if not chunk:
        break
    text+=chunk
    print(chunk)
file.close()
print('-'*20)
print(text)    


file=open('hello.text','r')
s=file.read()
file.close()
print(s)

with open('hello.text','r') as file:
    s=file.read()
    print(s)

a=[1,2,3,4]
with open('array1.txt','w') as file:
    file.write(str(a))
print(str(a))    
    
    
with open('array1.txt','r') as file:
    b=file.read()
    print(type(b),b)
    c=list(b)
    print(type(c),c)
    
import pickle
name='qwer'
age=22
address='미국'
arr=[1,2,3,4]
scores={
    'k':1,
    'k2':2
}
with open('pickle.p','wb') as f:
    pickle.dump(name,f)
    pickle.dump(age,f)
    pickle.dump(address,f)
    pickle.dump(arr,f)
    pickle.dump(scores,f)
    
with open('pickle.p','rb') as f:
    p1=pickle.load(f) 
    p2=pickle.load(f) 
    print(p1)   
    print(p2,type(p2))
    p3=pickle.load(f)
    print(p3)
    p4=pickle.load(f)
    print(p4)
    p5=pickle.load(f)
    print(type(p5),p5)
    
    print(p5['k'])
 
#a 이어쓰기   
with open('hello.txt','a') as f:
    f.write('1234')
    # f.read()    
# +
# 쓰기 계열에 붙어있다면 읽기 가능해짐
# 읽기 계열에 붙어있다면 쓰기 가능해짐!

print('-'*20)
with open('word.txt','r') as file:
    words=file.read()
  
    finds=words.split()# 공백제거
    
    for word in finds:
        if 'c' in word:
            a=word.replace(',','').replace('.','')
            # a=word.find('c')
            # print(word.find('c'))
            
            print(a)
            
            
        #  print(word)
        #  tmp=word.split('c')
        #  if len(tmp)>1:
        #      a=word.split('.')
        #      b=''.join(a)
        #      c= b.split(',')
        #      d=''.join(c)
        #      print(d)
             
             
            
    # print(len())         
    # find를 이용하면 조금 더 편리할 순 있음
    
    # '''
    # split을 사용해도 되지만 find를 이용해서 다시 풀어보는 방향성으로 생각
    
    
    # '''
    
               

        

    
    
    # 마침표랑 콤마를 제거해야함
    # for a in words:
    # clear_word=words.strip(',.')
    # print(type(clear_word))
    
    # if 'c' in clear_word:
     
        # print(words)
        
  
   

     # 콤마와 점을 제거 성공
     
        # if clear_word 
        
        # print(clear_word)
    
        #잘 제거되었는지 확인 성공
        
   
       
    
        


    
 
    

# 
    
   
    
   
    
    

