print('-'*30)

with open('order.txt','r',encoding='utf-8') as file:
    # 파일은 읽어옴
    txt=file.read()
    # 주문 목록별로 자르기
    split_txt=(txt.split('\n'))
    # txtTtxt2=txt.split(',') #점을 기준으로 나누기 
    # print(txtTtxt2)
    
    # 자른거를 다시 재가공하기
    # 목록이 공백인것도 생각해야함

    total=0
    for word in split_txt:
     comma=word.split(',')
    #  print(comma)
     if len(comma)!=3:
        continue
    
    #  주문 목록별로 나누기
     목록=comma[0].strip()
     수량=comma[1].strip()
     가격=comma[2].strip()
     
     가격=가격.replace('원','')
     가격=int(가격)
     수량=int(수량)

            #  print(목록)
             
             # print(가격)


     if 가격>10000 or 가격<0 or 수량<0:
                continue
            
     주문금액=가격*수량
     total+=주문금액


    print(f'전체 매출은 {total}원입니다.')  
            
            
         
               
                

     
    
           

        #    가격이 음수면 그냥 버림
         

       
         
        
     



    
    
    # 여기서 수량이랑 가격은 정수형으로  변환해줘야함
     

        # 이상치 감지하기(수량 이상, 가격 이상체크)

        
        



    # print(type(가격))
    # 문자형 -> 숫자형으로 변환 필요함

    
   



    #    print(word)

     
     

     
     
       

       
  

    #    목록=txtTtxt[0]
    #    수량=txtTtxt[1]
    #    가격=txtTtxt[2]
    

  

 


    #  print(b)
    #  print(type(b))
   

    # txtList=txt.split('')
       



    # for word in txtList:
    #     pass
    # txtList2=txt.split('\n')
    #  3개의 항목으로 나눔
    #  if len(txtList2)!=3:
    #    continue
    # else:
       
    #      price=txtList2[0].strip('')
    #      counts=txtList2[1].strip('')
    #      quantity=txtList2[2].strip('')
    #      quantity2=txtList2[3].strip('')
    #      quantity3=txtList2[4].strip('')
    #      quantity4=txtList2[5].strip('')
    #      quantity5=txtList2[6].strip('')

    #      print(price)
    #      print(counts)
    #      print(quantity)
    #      print(quantity2)
    #      print(quantity3)
    #      print(quantity4)
    #      print(quantity5)

      
        # 각항목의 앞뒤 공백제거하는 과정`price=txtList2[0].strip('')
    
   

   

       

    
    

    
    


   
    
      

     
          
                                      

      
         


# 이러면 3개로 끊기는 이쁜 리스트 생성 성공

   
    

     





  



   
    
 


   
    # print(txt)
    # 콤마로 끊으면 좋아보임

    # 그러면 필요한건
    # 변수가 3개임
    # 상품,수량 가격순 
    
    
    



   
    
        
# 이상치 제거

      

          
          
         
       
    
    # print(txt)
 