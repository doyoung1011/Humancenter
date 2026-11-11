

# 피라미드 찍어보기

for i in range(6):
    for j in range(5-i):
        print('_',end="")
    for k in range(2*i+1):
         print("*",end="")    
    print()

'''

for i in range(5):
   # 공백부터 찍어야함
    for j in range(5-1-i):
      print('-',end='')
     
    for k in range(2*i+1):
      print('*',end='')
      
    print() 
'''
print('*'*100)

for i in range(6):
    for j in range(5+i):
        print('-',end="")
    for k in range(2*i+1):
         print('*',end='')
    print()      