from pathlib import Path
from fastapi import APIRouter
import pandas as pd
import traceback
import utill
router=APIRouter(tags=['엘라스틱 서치'])
from typing import Literal
from typing import Any
# 파일 읽고 출력하고 검증하고 출력하고

@router.get('/read/head')
# def read(fileName):
def read(fileName:Literal['movies.csv','tags.csv','ratings.csv']='movies.csv'):
    print('filename:')
    frame=utill.load_csv(fileName)
    if frame is None:
        return{
            'ERROR':'파일을 불러오지 못했습니다.'
        }
    '''
    head: 상위 몇개의 데이터만 추출함(기본값:5)
    astype: 형변환, 기본값: NumPy.int64
    to_dict: dict로 변환
    orient='records': 컬럼명:값 형태
                      기본값:dict:인덱스가 키가 된다.
    '''
    # 앞의 것만 뽑아서 딕셔너리로 바꿨다.
    preview=frame.head().astype(object).to_dict(orient='records') # 한 줄도 레코드라고 부름.
    return preview   

@router.get('/read/valid')
def valid():
    df_movies_=utill.load_csv('movies.csv')
    df_tags_=utill.load_csv('tags.csv')
    df_ratings=utill.load_csv('ratings.csv')
    
   
    '''
    dropna: N/A 즉 결측치가 없는 것
    
    '''
    notnull=df_movies_['movieId'].dropna()   # id가 없는걸 제거해라는 뜻
    
    '''
    set 타입의 속성을 이용해서 id 중복을 제거함
    '''
    movie_ids=set(notnull)
    
    tag_ids=set(df_movies_['movieId'].dropna())
    rating_ids=set(df_ratings['movieId'].dropna())
    
    result={
       
    }
    result['no_id']={}
    result['no_id']['tags']=len(tag_ids-movie_ids)
    result['no_id']['ratings']=len(rating_ids-movie_ids)
    
    result['rating range']={}
    result['rating range']['min']=float(df_ratings['rating'].min())
    result['rating range']['max']=float(df_ratings['rating'].max())
    
    return result
 
def makeContent():
    df_movies=utill.load_csv('movies.csv')
    df_tags=utill.load_csv('tags.csv')
    
    # pands
    # 데이터 프레임: 2차원 배열
    # 시리즈: 1차원 값
    
    result=pd.DataFrame()
    result['movieId']=df_movies['movieId']   
    # pandas 타입을 string 타입으로 변경 후 앞 뒤 공백 제거
    result['title']=df_movies['title'].astype(str).str.strip()
    
    # 장르는 a|b|c 형식으로 되어있다
    # 그래서 list로 바꾸겠다
    
    def parse_genre(genres):
        result=[]
        if str(genres).strip()=='' or str(genres).strip()=='(no genres listed)':
             return result
         
        list_genre=str(genres).split('|')
        for genre in list_genre:
            # strip: 앞 뒤 공백 제거
            # lower: 소문자로 바꿈
            result.append(genre.strip().lower())
        
        return result
    
    """
    장르의 리스트가 쌓인다.
    """
    result['list_genre']=df_movies['genres'].map(parse_genre)
    # copy(): 원본을 보존하고 사본을 가져온다.
    tags=df_tags[ ['movieId','tag'] ].copy()
    # 공백 제거후 소문자로 변환
    tags['tag']=tags['tag'].astype(str).str.strip().str.lower()
    
    # group by 처럼 중복제거
    tags=tags.drop_duplicates(['movieId','tag'])
    
    #  pandas의 data frame 특성인데 컬럼이 아니라 True인 것반 반복 시킨다
    # tags=tags[tags['tag']!=''].drop_duplicates(['movieId','tag'])
    # print(tags.head())
    movie_tags={}
    # return tags
    for info in tags.to_dict(orient='records'):
        id=info['movieId']
        tag=info['tag']
        
        if id not in movie_tags:
            movie_tags[id]=[]
        movie_tags[id].append(tag)  

    # data frame인 tags를 movieId로 group by 해서
    # group by 한 거셍서 tag 항목을 꺼내고
    # agg(list): 결과를 lsit로 만들어서 
    
    '''
     to_dict()까지 한 결과
     {
         movieId1:[tag1,tag2],
         movieId2:[tag11,tag12]
     }
    
    '''
    
    movie_tags=tags.groupby('movieId')['tag'].agg(list).to_dict()
    
    # 태그가 안달린 영화는 빈 배열이 나올 꺼임
    # get 으로 안전하게 가져옴  
    result['list_tag']=df_movies['movieId'].map(lambda id : movie_tags.get(id,[]))       
    
    '''
    파이썬의 리스트는 +를 제공한다
    [1,2] + [3,4] == [1,2,3,4]
    '''
    # list_temp=[result['title']]+result['list_genre']+result['list_tag']
    # content_text=" ".join(list_temp)
    
    '''
    map: 한 컬럼을 대상으로 반복
    apply: 모든 컬럼을 대상으로 반복
    
    axis: 기본값 0
              0:위에서 아래로 읽기
              1:왼쪾에서 오른쪽으로
    
    '''
    
    result['content_text']=result.apply(
        lambda info: ' '.join([info['title']]+info['list_genre']+info['list_tag']).strip(),
        axis=1        
    )
    # reset_index는 pands 내부 indexfmf 재정리한다
    # drop=True 를 안함녀 새로 추가되어버림....
       
   
    
    return result.reset_index(drop=True)
    
@router.get('/make/content')
def content():
    dataFrame=makeContent()    
    return dataFrame.head(10).to_dict(orient='records')
# if __name__ == '__main__' :
#     print('Path(__file__):', Path(__file__))
#     load_csv('movies.csv')


def makeChunk():
    size_chunk=50
    overlap:int=15
    chunks:list[dict[str,Any]]=[]

    dataFrame=makeContent()
    content=dataFrame.to_dict(orient='records')

    step=size_chunk - overlap
    
    for info in content:
        text=info.get('content_text','').strip()
        if not text:
            continue
        
        '''
        0부터 
        
        '''
        
        
        # for idx_start in range(0,len(text),step):
        for idx,idx_start in enumerate(range(0,len(text),step)):
            chunk=text[idx_start:idx_start+size_chunk] # n번쨰부터 그 앞까지
            
            if chunk:
                chunks.append({
                   'movieId': int(info['movieId']),
                    'title':str(info['title']),
                    'genres':list(info['list_genre']),
                    'tags':list(info['list_tag']),
                    'content':chunk,
                    'chunk_index':idx
                })
                
    return chunks

@router.get('/make/chunk')
def chunk() :
    return makeChunk()[0:10] # dict 중에서 앞의 10개만 보여주겠다.             
        
def embedding_with_gemini(data):
    pass

def embedding_with_gpt(data):
    pass        
              
    
    
    
    
    
