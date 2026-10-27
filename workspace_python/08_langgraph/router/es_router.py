

from pathlib import Path
from fastapi import APIRouter,Query
import pandas as pd
import traceback

from typing import Literal
from typing import Any
from fastapi import APIRouter
import traceback
import utill
import pandas as pd
from typing import Any, Literal
import os 
from elasticsearch import helpers

from collections import Counter
import math

router = APIRouter(tags=["엘라스틱서치"])


@router.get("/read/head")
# def read(fileName) :
def read(fileName: Literal['movies.csv', 'tags.csv', 'ratings.csv'] = 'movies.csv'):
    print('fileName :', fileName)
    frame = utill.load_csv(fileName)

    if frame is None:
        return {'ERROR': "파일을 불러오지 못했습니다"}

    '''
    head : 상위 몇 개의 데이터만 추출 (기본값 : 5)
    astype : 형변환, 기본값:NumPy.int64
    to_dict : dict로 변환
    orient='records' : 컬럼명:값 형태
    기본값=dict : 인덱스가 키가 된다
    '''
    preview = frame.head().astype(object).to_dict(orient='records')
    return preview


@router.get('/read/valid')
def valid():
    df_movies = utill.load_csv('movies.csv')
    df_tags = utill.load_csv('tags.csv')
    df_ratings = utill.load_csv('ratings.csv')

    # pandas에서 movieId를 전체 select
    # dropna : N/A(Not Available) 결측치, 즉 없는걸 제외해라
    notnull = df_movies['movieId'].dropna()

    # set 타입의 속성을 이용해서 id 중복 제거
    # set 타입은 json, list와 다르게 중복을 관리해 줌 { 1, 2 } key만 있는 것
    movie_ids = set(notnull)
    tag_ids = set(df_tags['movieId'].dropna())
    rating_ids = set(df_ratings['movieId'].dropna())

    # 중복되지 않은 ID가 있다면 길이를 체크하여 표시
    result = {}
    result['no_id'] = {}
    result['no_id']['tags'] = len(tag_ids - movie_ids)
    result['no_id']['ratings'] = len(rating_ids - movie_ids)

    # 별점의 min, max 확인
    result['rating range'] = {}
    result['rating range']['min'] = float(df_ratings['rating'].min())
    result['rating range']['max'] = float(df_ratings['rating'].max())

    return result

# 제목+장르들
def makeContent():
    df_movies = utill.load_csv('movies.csv')
    df_tags = utill.load_csv('tags.csv')

    # pandas
    # 데이터 프레임 : 2차원 배열
    # 시리즈(1줄 씩) : 1차원 값
    result = pd.DataFrame()
    result['movieId'] = df_movies['movieId']

    # df에서는 str로 형변환 해준 뒤에 strip해야 적용 됨
    result['title'] = df_movies['title'].astype(str).str.strip()

    # 장르는 a|b|c 형식으로 되어있다
    # 그래서 list로 바꾸겠다.
    def parse_genre(genres):
        result = []

        if str(genres).strip() == '' or str(genres).strip() == '(no genres listed)':
            return result

        list_genre = str(genres).split('|')

        for genre in list_genre:
            result.append(genre.strip().lower())

        return result

    # 장르의 리스트가 쌓임 (parse_genre에서 공백제거 후 담은것을)
    # pandas에서도 map을 제공해줌
    result['list_genre'] = df_movies['genres'].map(parse_genre)

    # 배열을 주면 여러 개의 컬럼을 가져올 수 있다
    # pandas에서도 깊은복사 copy()를 제공
    tags = df_tags[['movieId', 'tag']].copy()
    tags['tag'] = tags['tag'].astype(str).str.strip().str.lower()

    # pandas에서는 group by 처럼 중복을 제거해주는 함수가 제공됨
    tags = tags.drop_duplicates(['movieId', 'tag'])

    # pandas의 data frame 특성인데, 리스트 안에 컬럼이 아니라 True인것만 반복 시킬 수 있음
    # tags = tags[tags['tag'] != ''].drop_duplicates(['movieId', 'tag'])

    # print(tags.head())
    # return result

    movie_tags = {}

    # df를 딕셔너리로 변환
    for info in tags.to_dict(orient='records'):
        id = info['movieId']
        tag = info['tag']

        # dict의 key중에서 id가 없다면 key를 id로 추가 후 빈 list로
        if id not in movie_tags:
            movie_tags[id] = []

        movie_tags[id].append(tag)

    # 위 코드를 한 줄로 줄이면 아래처럼 할 수 있음
    # pandas 에는 groupby를 제공함, groupby한 tag를 list로 형변환하고 dict로 변환
    # tags.groupby('movieId') : data frame인 tags를 movieId로 groupby
    # ['tag'] : groupby한 것에서 tag항목을 꺼내고
    # agg(list) : 꺼낸 항목을 list로 만들어서
    # to_dict() : 딕셔너리로 변환
    '''
    to_dict() 까지 한 결과
    {
        movidId1 : [tag1, tag2],
        movieId2 : [tag11, tag12]
    }
    '''
    movie_tags = tags.groupby('movieId')['tag'].agg(list).to_dict()

    # print(movie_tags)

    # 람다를 사용해서 df_movies의 movieId를 전부 돌면서 movie_tags에서 해당하는 tag를 result['list_tag'] 에 저장
    # lambda는 넣게되면 하나하나 돌면서 lambda가 작동되기 때문에 이후 체이닝, 리턴 등 값으로 추가 작업할 수 있음
    # -> 그때그때 처리해야 하는 일들을 풀어 적어놓고, 그때그때 동작하도록 (지금 동작하는 당시의)
    result['list_tag'] = df_movies['movieId'].map(
        lambda id: movie_tags.get(id, [])
    )

    # 파이썬의 리스트는 +를 제공
    # [1,2] + [3,4] == [1,2,3,4]
    # list_temp = [result['title']] + result['list_genre'] + result['list_tag']
    # content_text = ' '.join(list_temp)

    # map() : 한 컬럼을 대상으로 반복
    # apply() : 모든 컬럼을 대상으로 반복 (axis : 축)
    # axis : 기본값은 0
    # 0 : 위에서 아래로 읽기
    # 1 : 왼쪽에서 오른쪽으로
    result['content_text'] = result.apply(
        lambda info: ' '.join(
            [info['title']] + info['list_genre'] + info['list_tag']
        ).strip(),
        axis=1
    )

    # * : 언팩킹, js의 ...와 같음
    # 배열을 하나씩 분리해 주는 것
    # *[1,2,3] = 1,2,3
    # result['content_text'] = result.apply(
    #     lambda info : ' '.join([info['title']] , *info['list_genre'] , *info['list_tag']).strip(),
    #     axis=1
    # )

    # reset_index : pandas 내부 index를 재정리
    # drop=True를 안 해주면, 132 라고하면 123이 아니라 1323이 되는것을 막기 위함 (새로 추가됨)
    # → 엉망인 것은 버려라
    return result.reset_index(drop=True)


@router.get('/make/content')
def content():
    # result는 data frame이기 때문에 dict로 변환해서 return
    dataFrame = makeContent()
    return dataFrame.head(10).to_dict(orient='records')
'''
한줄로 만들어진 content_text를 적당히 쪼개고 겹쳐서 chunk로 만들기

'''


def makeChunk():
    size_chunk = 50
    overlap: int = 15

    # 자료형을 미리 지정하기 chunks = []
    # Any를 import해서 object처럼 아무거나 들어와도 되도록 사용할 수 있음
    chunks: list[dict[str, Any]] = []

    dataFrame = makeContent()
    content = dataFrame.to_dict(orient='records')

    step = size_chunk - overlap

    for idx_content, info in enumerate(content):
        text = info.get('content_text', '').strip()

        if not text:
            continue

        # for idx_start in range(0, len(text), step):
        for idx, idx_start in enumerate(range(0, len(text), step)):
            chunk = text[idx_start:idx_start + size_chunk]

            if chunk:
                chunks.append({
                    'index': idx_content,
                    'movieId': int(info['movieId']),
                    'title': str(info['title']),
                    'genres': list(info['list_genre']),
                    'tags': list(info['list_tag']),
                    'content': chunk,
                    'chunk_index': idx
                })

    return chunks


@router.get('/make/chunk')
def chunk():
    return makeChunk()[0:10]


@router.get('/make/embedding/gemini')
def embedding():
    target = makeChunk()[0:10]
    actions = utill.embedding_with_gemini(target)

    return actions


@router.get('/make/embedding/openai')
def embedding():
    target = makeChunk()[0:10]
    # target = makeChunk()
    actions = utill.embedding_with_openai(target)

    return actions

'''
벌크 하기 전에 헬스 체크부터 먼저해봅시다


'''
@router.get('/es/health')
def health():
    return{
        'msg':utill.es.ping()
    }






@router.post('/es/bulk')
def bulk():
    target = makeChunk()
    actions = utill.embedding_with_openai(target)
    
    '''
    1.만약에 엘라스틱 서치에 인덱스가 없다면 새로 만들기
    2. 있으면 bulk로 넣기
    ES_INDEX
    '''
  
    
    if not utill.es.indices.exists(index=os.getenv('ES_INDEX')): #인덱스가 없다면
        utill.es.indices.delete(index=os.getenv('ES_INDEX'))
        
    if not utill.es.indices.exists(index=os.getenv('ES_INDEX')):
        
        
        
        '''
        #기본 chunk 구조
        chunks.append({
                        'index': idx_content,
                        'movieId': int(info['movieId']),
                        'title': str(info['title']),
                        'genres': list(info['list_genre']),
                        'tags': list(info['list_tag']),
                        'content': chunk,
                        'chunk_index': idx
                    })
        
        
        '''
        
        mappings={
            'properties':{
                'index':{'type':'integer'},
                'moveid':{'type':'integer'},
                'title':{'type':'text'}, #keyword: 완벽히 같은 단어 검색 용
                'genres':{'type':'keyword'},
                'tags':{'type':'text'},
                'content':{'type':'text'}, # text: 형태소를 이용한 유용한 검색용
                'chunk_index':{'type':'integer'}, # text: 형태소를 이용한 유용한 검색용
                
                'embedding':{
                    'type':'dense_vector',
                    'dims':768
                }       
                
            }
        }
        utill.es.indices.create(
            index=os.getenv('ES_INDEX'),
            mappings=mappings
        )
    #  bulk로 넣기
    
    success,errors=helpers.bulk(
        utill.es,
        actions,
        stats_only=False, # 성공, 실패 숫자와 메세지
        raise_on_error=False
        
    )
    return {
        'msg':{
            'succ':success,
            'errors':errors
        }
    }    


'''
^ 웃는 표시가 가중치를 준다는 뜻임

'''


def search_movies(keyword:str,size:int=10):
    response=utill.es.search(
        index=os.getenv('ES_INDEX'),
        query={
            'multi_match':{
                'query':keyword,
                'fields':['title^300','genres^2','tags','content'],
             
            },
            
        }
        ,size=size
    )
    
    return response

@router.get('/es/select/multi_match')
def multi_match(keyword,size=10):
    response=search_movies(keyword,size)
    
    return{
        'msg':utill.formatter(response)
    }
    


def term_movieId(ids:list):
    '''
    term: 키워드 where id= 1 
    terms: 리스트 where id in (1,2,3) 이런 느낌
    '''
    response=utill.es.search(
        index=os.getenv('ES_INDEX'),
        query={
            'terms':{
                'movieId':ids
            }
            
        }
        ,size=len(ids)*5
    )
    
    return response    

@router.get('/es/select/terms')
def terms(ids:list=Query(...)):
    response=term_movieId(ids)
    
    return{
            'msg':utill.formatter(response)
        }
        
#####################
## 추천 시스템
#####################       


@router.get('/recommend/test/counter')
def test_counter():
    str='hello world'
    print(Counter(str))
    
    list_counter=['hi','hey','hi','hello','hi','nihao','hey']
    print(Counter(list_counter))
   
    food_counter=Counter()
    list_food=['김밥','달빵','마라탕','라면','김밥','초밥','달빵']
    for food in list_food:
        food_counter.update(food)
    print(food_counter)
    #Counter({'밥': 3, '김': 2, '달': 2, '빵': 2, '라': 2, '마': 1, '탕': 1, '면': 1, '초': 1})
    
    food_counter2=Counter()
    for food in [list_food]:
        food_counter2.update(food)
    print(2,food_counter2)
    '''
    
    Counter({'밥': 3, '김': 2, '달': 2, '빵': 2, '라': 2, '마': 1, '탕': 1, '면': 1, '초': 1})
    2 Counter({'김밥': 2, '달빵': 2, '마라탕': 1, '라면': 1, '초밥': 1})
    '''
    
    favorite_foods=[
        ['밥','치킨'],
        ['산낙지','육회','광어회'],
        ['밥','라면','짜장면'],
        ['햄버거','라면','밥']
    ]
    food_counter3=Counter()
    for foods in favorite_foods:
        food_counter3.update(foods)
        print(food_counter3)
    
    # CBF 콘텐츠 기반 필터링 content-Based Filtering
    # "내가 뭘 좋아했지?" 기반으로 추천
    
def content_based_filtering(list_movieid:list):
    selected=term_movieId(list_movieid)   
    # return selected
    
    genre_counter=Counter()
    tag_counter=Counter()
    for hit in selected['hits']['hits']:
        source=hit['_source']
        print(source)
        genre_counter.update(source.get('genres',[]))
        tag_counter.update(source.get('genres',[]))
    
    print('genre_counter',genre_counter)    
    print('tag_counter',tag_counter)
    
    '''
    장르와 태그를 각각 집계한뒤: Counter
    most_common: 기본값 None   

    '''
    
    
    max=5
    terms_genre=[term for term, count in genre_counter.most_common(max)]
    
    terms_tag=[term for term, count in tag_counter.most_common(max)]
    terms=terms_genre+terms_tag
    
    terms=[]
    terms.extend(terms_genre)
    terms.extend(terms_tag)
    
    # return terms
    #  " ".join(terms) 이거의 단점은 중복 데이터가 있을 수 있음...
    #그래서 set에 넣어보자
    # 그런데 순서를 보장하지 않는다.
    # 나는 순서를 유지하면서 중복을 제거하고 싶다
    # dict.fromkeys()를 사용하면 된다
    # 이걸 join하면 key만 뺴올 수 있다.
    query=" ".join(dict.fromkeys(terms)) #띄어쓰기로 구분한다
    response=search_movies(query) 
    
    return response['hits']['hits']       
        

@router.get('/recommend/cbf')
def cbf(list_movieid:list[int]=Query(...)):
    response=content_based_filtering(list_movieid)      
    
    return response    


def split_train_test(test_size: float = 0.2):

    '''
    과거 평점을 학습시키고 미래 평점으로 평가하자
    test_size: 미래 평점의 비율(정답 데이터의 비율)

    사용자 별로 최신 평점은 평가용
    최신 평점은 평가용
    과거 평점은 학습용(공부할때는 과거의 것으로 공부하고)

    시험은 최신 껄로 보겠다.

    평점이 한 건뿐인 사용자는 학습 데이터에만 둔다.

    만약에 timestamp가 같으면 원본 행 순서로 정렬한다.
    '''

    # 평점 파일 읽기
    frame_ratings = utill.load_csv('ratings.csv')

    # 원본 유지를 위해
    data = frame_ratings.copy()

    # 원본의 순서대로 줄 번호 먹이기
    data['original_order'] = range(len(data))

    # timestamp를 숫자 타입으로 변경
    # errors='coerce': 변경이 안되는건 NaN으로 강제 변경
    # errore='ignore': 변경 실패 시 원본 유지
    # errors='raise': ValueError 발생하고 즉시 중단
    valid_data = pd.to_numeric(data['timestamp'], errors='coerce')  # vaild 유효한

    # N/A가 아닌 것만 뽑아준다
    # data[True/False] >>>> 참인 행(row 또는 document)만 반환
    valid_data = data[data['timestamp'].notna()].copy()

    # 시간이 N/A 즉 비어있는 것만 뽑아준다
    no_time = data[data['timestamp'].isna()].copy()
    
    test_indices=[]
    
    # userid가 같은 데이터끼리 group by
    # sort 기본값은 True >> userId로 정렬하지 않고 원래 등장 순서를 유지
    # 원래 id,value 반환인데 id는 안 쓸거라서
    for _, group in valid_data.groupby('userId', sort=False):

        # 평점을 하나만 준 사용자는 건너뛰기
        # 지금은 학습과 정답 데이터를 나누는 거라서
        if len(group) <= 1:
            continue

        # 과거와 미래를 나누기 위해서
        # timestamp 기준으로 정렬한다
        # 같은게 있다면 original_order 기준으로 정렬하라.
        # kind stable: 그래도 같은게 있다면 정렬 전 순서 유지.
        # kind에 사용할 수있는것
        # quicksort,mergesort,heapsort,
        
        ordered = group.sort_values(
            ['timestamp', 'original_order'],
            kind='stable'
        )

        # 전체 데이티ㅓ 중 test_size 비율로 뽑았다
        # 0.4 등의 결과를 1로만든다
        test_counter = math.ceil(len(ordered) * test_size)

        if test_counter < 1:
            test_counter = 1

        if test_counter > len(ordered) - 1:
            temtest_counterp1 = len(ordered) - 1

        # max: 둘 중에 큰 값ㅇ르 돌려준다
        # 최소값을 지정할 떄 사용
        max(1, test_counter)
        
        # min: 둘 중에 작은 값을 돌려준다
        # 최대값을 지정할 때 사용
        min(test_counter,3)
        
        test_counter=min(len(ordered)-(1,math.ceil(len(ordered)*test_size)))
        
        # tail: 끝에서 몇개 
        # 미리 시간 오름차순으로 정렬해 둬서 최신 데이터는 끝에 있다.
        # index만 모은다- 나중에 학습 데이터를 분리 할때 사용하려고
        
        test_indices.extend(ordered.tail(test_counter).index.tolist())
        
    '''
    데이터 할 데이터의 index는 모아둔 상태
    실제 테스트 데이터 추출 예정
    학습 데이터 추출 예정
    2개를 리턴 할 예정
    
    '''
        
        
        
