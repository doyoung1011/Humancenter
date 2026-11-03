from fastapi import APIRouter,Query
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI
from google import genai
from google.genai import types
import os 
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import SystemMessage,HumanMessage,AIMessage 
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from pydantic import BaseModel

from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser

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
 
class Recipe(BaseModel):
    food:list[str]
    steps:list[str]
    
    
    
@router.get('/langchain/output_parser')
def ouput_parser(dish:str):
    ouput_parser=PydanticOutputParser(pydantic_object=Recipe)
    
    prompt=ChatPromptTemplate.from_messages([
        (
            "system",
            "사용자가 입력한 요리의 레시피를 알려주세요"
            '{format_instructions}'
            # 콤마 없음...
        ),
        ("human","{dish}")
    ])
    prompt2=prompt.partial(format_instructions=ouput_parser.get_format_instructions()
    )
    prompt_value=prompt2.invoke({
        "dish":dish
    })
    print(prompt_value)
    
    print('*'*50)
    
    model=ChatOpenAI(
              model='gpt-5.5',
              temperature=0,
              api_key=os.getenv('OPENAI_API_KEY')
          )
    ai_msg=model.invoke(prompt_value)
    print(ai_msg)
    
    result=ouput_parser.invoke(ai_msg)
    
    return result


@router.get('/langchain/str_output_parser')
def str_ouput_parser(dish:str):
    model=ChatOpenAI(
            model='gpt-5.5',
            temperature=0,
            api_key=os.getenv('OPENAI_API_KEY')
        )
    ai_msg=model.invoke(f'{dish}의 레시피를 간략하게 알려주라')
    
    # result=StrOutputParser().parse(ai_msg) # 전문 모두 나옴
    result=StrOutputParser().invoke(ai_msg) # content만 나옴
    return result


@router.get('/langchain/chain')
def str_ouput_parser(name:str,dish:str):
     prompt_template=ChatPromptTemplate.from_messages([
             ("system","너는 친절한 조수야"),
             ("human","나는 {name}이야"),
             ("ai", "안녕하세요! {name}님. 친절하게 알려드리겠습니다"),
             ("human",'{prompt}')
 ])
     
     model=ChatOpenAI(
                          model='gpt-5.5',
                          temperature=0,
                          api_key=os.getenv('OPENAI_API_KEY')
                      )
     
     chain=prompt_template | model | StrOutputParser() 
     result=chain.invoke({
         "name":name,
         "prompt":f'{dish}의 레시피를 간단히 알려줘'
     })
     
     return result 
 
@router.get('/langchain/chain/pydantic')
def chain_pydantic(name:str,dish:str):
    
    ouput_parser=PydanticOutputParser(pydantic_object=Recipe)
    
    prompt=ChatPromptTemplate.from_messages([
        ('system',
        '너는 미슐랭 쉐프야. 나는 요리 초보고 자취생이라 기구가 거의 없어.'
        '내가 쉽고 빠르게 만들 수 있는 레시피를 알려주라'
        '{format_instructions}'),
        ('human','{dish}')
    ]).partial(format_instructions=ouput_parser.get_format_instructions()
    )
    model=ChatOpenAI(
                     model='gpt-5.5',
                     temperature=0,
                     api_key=os.getenv('OPENAI_API_KEY')
                 ).bind(
                #리턴 형식을 json으로 지정해준건데, 된다는 보장은 없다.     
                response_format={
                    'type':'json_object'
                }
            )
    
    chain=prompt | model | ouput_parser
    result=chain.invoke({
        "dish":dish
    })
    
    return result

@router.get('/langchain/chain/with_structured_output')
def chain_pydantic(dish:str):
    
    
    prompt=ChatPromptTemplate.from_messages([
        ('system',
        '너는 미슐랭 쉐프야. 나는 요리 초보고 자취생이라 기구가 거의 없어.'
        '내가 쉽고 빠르게 만들 수 있는 레시피를 알려주라'
        ),
        ('human','{dish}')
    ])
    model=ChatOpenAI(
                         model='gpt-5.5',
                         temperature=0,
                         api_key=os.getenv('OPENAI_API_KEY')
                     )
    
    chain=prompt | model.with_structured_output(Recipe)
    
    return chain.invoke({
        "dish":dish
    })
 
 
 
##############################
## CF 추천 끼워넣기
############################# 
from router import es_router
@router.get('/langchain/recommend/hybrid')
def gpt_rangchain(userId:int, # CF에서 사용 할 사용자 ID
        provider:Literal['gemini','gpt']='gpt',
        top_k:int=10, # 결과 개수
        candidate_size:int=50,# 각각의 추천의 후보 수     
        list_movieId:list[int]=Query(...),
    ):
    '''
    이전에 만들어 놓았던 hybrid 추천 결과를 그대로 가져와서 
    langchain으로 LLM에게 이쁘게 포장해라 말라고 해서 그 결과를 출력한다.
    단,사용자가 gpt랑 제미나이를 고르게 만든다.
    '''
    
    hybrid=es_router.hybrid(userId,top_k,candidate_size,list_movieId)
    
    prompt=ChatPromptTemplate.from_messages([
            ('system',
            '너는 영화 추천전문가야. 나는 영화를 잘몰라.'
            '장르랑 영화를 쉽게 추천해주라'
            ),
            ('human','{provider}')
        ])
    if provider=='gpt':
         model=ChatOpenAI(
                model='gpt-5.5',
                temperature=0,
                api_key=os.getenv('OPENAI_API_KEY')
                )
    elif provider=='gemini':
        model=ChatGoogleGenerativeAI(
                model='gemini-3.8-flash', 
                temperature=0.0,
                api_key=os.getenv('GEMINI_API_KEY')  
            )
    
    
    chain=prompt | model
    
    return chain.invoke({
        "provider":provider
    })
   