from fastapi import APIRouter
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI
from google import genai
from google.genai import types
import os 
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import SystemMessage,HumanMessage,AIMessage 
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

router = APIRouter(tags=["langchain"])
load_dotenv()


#  그냥 gpt에 말 걸기- 단발성임
@router.get('/langchain/gpt')
def gpt(prompt:str):
    model=ChatOpenAI(
        model='gpt-5.5',
        temperature=0,
        api_key=os.getenv('OPENAI_API_KEY')
    )
    output=model.invoke(prompt)
    return output
# 멀티턴으로 gpt에 말하기, langchain 모듈 사용!
@router.get('/langchain/gpt/multi')
def gpt2(prompt:str):
    model=ChatOpenAI(
          model='gpt-5.5',
          temperature=0,
          api_key=os.getenv('OPENAI_API_KEY')
      )
    
    messages=[
        {"role":"system","content":"너는 친절한 조수야"},
        {"role":"user","content":"나는 도영이야"},
        {"role":"assistant","content":"안녕하세요! 도영님. 친절하게 알려드리겠습니다"},
        {"role":"user","content":prompt}
    ]
    
    output=model.invoke(messages)
    return output

# openAi 모듈을 사용했다.
@router.get('/original/gpt')
def gpt2(prompt:str):
    client=OpenAI(api_key=os.getenv('OPENAI_AI_KEY'))
    
    messages=[
            {"role":"system","content":"너는 친절한 조수야"},
            {"role":"user","content":"나는 도영이야"},
            {"role":"assistant","content":"안녕하세요! 도영님. 친절하게 알려드리겠습니다"},
            {"role":"user","content":prompt}
        ]
    
    output=client.chat.completions.create(
        model='gpt-5.5',
        messages=messages,
        # temperature=0,
    )
    
    """
    실제 대답은 choice에 있는 message에 있는 content에 있음. 
    choice[0].message.content에 들어있다.
    
    """
    return output





#genai 모듈을 사용
@router.get('/langchain/gemini1')
def gemini(prompt:str):
    # 쌩으로 genai 모듈 사용법
    client=genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
    # gemini는 사용할때 role에 system이 없음
    # parts로 적여야함
    messages=[
                {"role":"user","parts":[{'text':'나는 도영이야'}]},

                {"role":"model","parts":[{'text':'안녕하세요! 도영님. 친절하게 알려드리겠습니다'}]},
                {"role":"user","parts":[{'text':prompt}]}
            ]
    
    output=client.models.generate_content(
        model='gemini-3.8-flash',
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction='너는 친절한 조수야',
            temperature=0.0
        )
    )
    '''
    실제 대답은  candidates[0].content.parts[0].text에 숨겨져있다.
    
    '''
    
    return output
    
@router.get('/langchain/gemini2')
def gemini(prompt:str):
    model=ChatGoogleGenerativeAI(
        model='gemini-3.8-flash', 
        temperature=0.0,
        api_key=os.getenv('GEMINI_API_KEY')  
    )
    messages=[
        {"role":"system","content":"너는 친절한 조수야"},
        {"role":"user","content":"나는 도영이야"},
        {"role":"assistant","content":"안녕하세요! 도영님. 친절하게 알려드리겠습니다"},
        {"role":"user","content":prompt}
    ]
    
    output=model.invoke(messages)
    # 실제 대답은 output.content[0].text에 들어있다
    return output
    
            
@router.get('/langchain/gpt4')
def gpt2(prompt:str):
    model=ChatOpenAI(
          model='gpt-5.5',
          temperature=0,
          api_key=os.getenv('OPENAI_API_KEY')
      )
    # provider에 따라 형식을 맞춰준다.
    
    messages=[
    SystemMessage('너는 친절한 조수야'),
    HumanMessage('내 이름은 도영이야'),
    AIMessage('안녕하세요. 도영님. 친절하게 알려드리겠나이다'),
    HumanMessage(prompt)
    ]
    
    output=model.invoke(messages)
    return output


# langchain의 message 모듈 사용해서 질문하기 
@router.get('/langchain/gpt/message')
def gpt2(prompt:str):
    model=ChatOpenAI(
          model='gpt-5.5',
          temperature=0,
          api_key=os.getenv('OPENAI_API_KEY')
      )
    # provider에 따라 형식을 맞춰준다.
    
    messages=[
    SystemMessage('너는 친절한 조수야'),
    HumanMessage('내 이름은 도영이야'),
    AIMessage('안녕하세요. 도영님. 친절하게 알려드리겠나이다'),
    HumanMessage(prompt)
    ]

    for chunk in model.stream(messages):
        print(chunk.content,end="",flush=True)
   
@router.get("/langchain/gpt/chat_prompt_template")
def chat_promt_tempalte(name:str,prompt:str):
     
 prompt_template=ChatPromptTemplate.from_messages([
             ("system","나는 도영이야"),
             ("human","나는 {name}이야"),
             ("ai", "안녕하세요! {name}님. 친절하게 알려드리겠습니다"),
             ("human",'{prompt}')
 ])  
 
 prompt_template.invoke({
     "name":name,
     "prompt":prompt
 })
 
 print(prompt_template)



@router.get("/langchain/gpt/messages_placeholder")
def chat_promt_tempalte(name:str,prompt:str):
     
 prompt_template=ChatPromptTemplate.from_messages([
             ("system","너는 친절한 조수야"),
             MessagesPlaceholder("history",optional=True),
             ("human",'{prompt}')
 ])  
 
 prompt_template.invoke({
     "history":[
         HumanMessage("내 이름은 도영이다."),
         AIMessage("안녕하세요. 도영님 친절히 알려드립니다")
     ],
     "prompt":prompt
 })
 
 print(prompt_template)
                