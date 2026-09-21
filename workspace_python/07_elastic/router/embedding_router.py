from fastapi import APIRouter
from elasticsearch import helpers

# 정규 표현식(regular expression, regExp) 사용을 위한 모듈
import re
from util import es, load_documents
router = APIRouter(tags=['임베딩 관련 라우터'])


@router.get('/embed/split')
def split(text):
    return split_text(text)


def split_text(text):
    print('text:', text)

    sentences = re.split(
        r"(?<=[.!?])\s+",  # .!? 뒤의 공백을 기준으로 분리
        text.strip()
    )

    print('sentences:', sentences)

    # 빈 문자열 제거
    sentences2 = []

    for s in sentences:
        if s.strip():
            sentences2.append(s.strip())

    sentences = sentences2

    chunks = []
    chunk_size = 10
    
    
    #청크보다 작은 문장은 합칠 수 있으면 합치자
    # 큰 건 어쩔 수 없고
    # 임시 저장소
    temp = ''

    for sentence in sentences:
        print('길이, 글씨:', len(sentence), sentence)

        # 일단 다음 문장을 붙여본다.
        if len(temp) > 0:
            candidate = f'{temp} {sentence}'
        else:
            candidate = sentence

        # 붙인 게 chunk_size 이하라면 temp에 계속 저장
        if len(candidate) <= chunk_size:
            temp = candidate

        # chunk_size를 넘어가면
        else:
            # 기존 temp가 있으면 먼저 저장
            if len(temp) > 0:
                chunks.append(temp)
            #     temp=''
            # elif len(temp)==0:
            #     chunks.append(sentence)
            
            temp=sentence
        if len(temp)>0:
            chunks.append(temp)
        print(chunks)
        
        overlap_size=6
        overlap_chunks=[]
        for index,chunk in enumerate(chunks):
            if index==0:
                overlap_chunks.append(chunk)
                continue
             
            prev=chunks[index-1]
            prefix=prev[-overlap_size:] #뒤에서 overlap_size 만큼부터 끝까지
            now=f'{prefix}{chunk}'.strip()
            overlap_chunks.append(now)
            
        print(overlap_chunks)
        return overlap_chunks

@router.post('/embed/create')
def create_embed_index():
    if es.indices.exists(index='computer_chunk'):
        es.delete_by_query(
            index='computer_chunk',
            query={
                'match_all':{} # 모든 문서 대상
            },
            refresh=True #삭제 결과를 즉시 검색에 반영함.
            
        )
        return 'computer_chunk가 이미 있습니다'
    
    es.indices.create(
        index='computer_chunk',
        mappings={
              'properties' : {
                               'id' : {'type' : 'integer'},
                               'title' : {'type' : 'text'}, #유연한값 :  백터로 분석해서 유연한 검색이 가능하다.
                               'category' : {'type' :  'keyword'},  # 정확한값 :  딱 완전 똑같은  단어로만 검색이 가능하다.
                               'price' : {'type' : 'integer'},
                               'rating' : {'type' : 'float'},
                               'created_at' : {'type' : 'date'},
                               'content' : {'type' : 'text'},
                               'embedding':{
                                   'type':'dense_vector',
                                   'dims':384 # 64의 배수라서 cpu 연산 단위와 호환이 잘된다
                                              # 512도 많이 쓴다 256은 뉘양스에 조금 약하다.
                               }
                           }
        },
    )
    
    return 'computer_chunk index 생성 완료'
        
@router.post('/embed/insert/bulk')
def ingest_embed_document():
    # json 가져오기
    documents=load_documents()
    actions=[]
    #  chunk 만들기
    for doc in documents:
        chunks=split_text(doc['content'])
        for index,chunk in enumerate(chunks):
            # 벡터로 변환하기
            embedding=get_embedding(doc['title',chunk])
        # 살짝 변형
        doc2=doc
        doc2['chunk_index']=index
        doc2['embedding']=embedding
        
        # actions에 추가
        
        actions.append({
            '_index':'computer_chunk',
            '_id':f'{doc2["id"]}-{index}',
            '_source':doc2
        })
    
    helpers.bulk(
        es,
        actions,
        stats_only=False #기본값 True
                         #True: 성공 실패 숫자만
                         #False:  성공 실패 숫자 + 에러 메세지 
        
    )

        
    
def get_embedding(title,content):
    text=f'title:{title}\ncontent:{content}'
    # 임베딩을 저장용으로 요청한다.
    result = es.inference.text_embedding(
    inference_id=".multilingual-e5-small-elasticsearch",
    input=text,
    input_type="ingest" # ingest: 저장할 떄 
                        # search: 검색할 때 
    )
    print('='*100)
    print(text)
    print(result)
    
    return result['text_embedding'][0]['embedding']


    
   
                    
                
            
            
            
            

  
    
    
    
    

        