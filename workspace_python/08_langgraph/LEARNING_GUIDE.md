# 08_langgraph 학습 정리 — 영화 검색·추천 시스템

> 실제 코드 기준: `api.py`, `utill.py`, `router/es_router.py`, `requirements.txt` (2026-11-02 확인)  
> **중요:** 폴더 이름은 `08_langgraph`이지만 현재 확인된 Python 코드에는 `StateGraph`, 노드/엣지 등 LangGraph 그래프 생성·실행 로직이 없습니다. 현재 핵심은 **검색·추천 시스템과 백엔드 API** 학습입니다.  
> 이 문서는 원본 코드를 건드리지 않고 **주요 실행 코드를 줄별 주석으로 풀어 쓴 학습용 문서**입니다. 아래 주석 포함 코드는 이해를 위한 발췌·재구성이며 원본과 다를 수 있습니다.

## 1. 나는 지금 무엇을 배우고 있나?

| 분야 | 실제 파일/함수 | 학습 목적 |
|---|---|---|
| FastAPI | `api.py`, `router/es_router.py` | GET/POST API, 라우터, 쿼리 파라미터 |
| Pandas | `load_csv`, `valid`, `makeContent` | CSV, 결측값, 중복, 그룹화, 데이터 가공 |
| 텍스트 청킹 | `makeChunk` | 겹치는 문자열 단위로 문서 분할 |
| LLM용 임베딩 | `embedding_with_gemini/openai` | 텍스트→768차원 벡터 변환 |
| Elasticsearch | `bulk`, `search_movies`, `search_vector` | 역색인·텍스트 검색·KNN 벡터 검색 |
| 콘텐츠 추천(CBF) | `content_based_filtering` | 사용자가 좋아한 영화의 장르/태그로 검색 |
| 협업 추천(CF) | `collaborative_filtering` | 유사 사용자 평점으로 예상 선호도 추정 |
| 모델 평가 | `split_train_test`, `recall_at_k` | 시간 순 학습/평가 분리, Recall@K |
| 혼합 추천 | `hybrid_filtering` | CBF + CF 순위를 RRF로 합치기 |

**전체 흐름:** MovieLens CSV → Pandas 정제 → 영화 제목·장르·태그 결합 → 겹치는 청크 → 임베딩 생성 → Elasticsearch 색인 → 검색/추천 API. 별도로 평점 데이터 → 사용자 기반 CF → CBF와 순위 융합까지 실습합니다.

## 2. 프로젝트 파일 역할과 실행 순서

- `api.py`: FastAPI 애플리케이션 엔트리포인트.
- `router/es_router.py`: CSV 조회, 문서 생성, 인덱싱, 검색, 추천 API.
- `utill.py`: CSV 로더, Gemini/OpenAI 임베딩, ES 클라이언트, 결과 변환 공통 기능.
- `data/ml-latest-small/`: MovieLens 학습 자료 (`movies.csv`, `tags.csv`, `ratings.csv`, `links.csv`).
- `requirements.txt`: 설치 의존성. **현재 코드에서 `surprise`를 import하지만 요구사항에 해당 설치 항목이 없습니다.** 설치 및 Python 환경 호환 여부 확인 필요.

### api.py — 한 줄씩

```python
from fastapi import FastAPI               # FastAPI 웹 애플리케이션 클래스 불러오기
from router.es_router import router as es_router  # 기능별 API가 들어 있는 라우터 불러오기
app = FastAPI()                            # 애플리케이션 객체 생성
app.include_router(es_router)              # 라우터의 모든 엔드포인트를 앱에 등록

@app.get('/')                              # GET / 요청이 들어오면 바로 아래 함수 실행
def home():                                # 루트 페이지 처리 함수 선언
    return "hello world!"                  # 응답 본문으로 문자열 반환

if __name__ == '__main__':                 # 이 파일을 직접 실행했을 때만 다음 코드 실행
    import uvicorn                         # ASGI 개발 서버 불러오기
    uvicorn.run('api:app', port=8000, reload=True, host='0.0.0.0')  # 8000포트로 실행하고 코드 변경 감지
```

`host='0.0.0.0'`는 모든 네트워크 인터페이스에서 접속을 받는다는 의미이므로 개발 환경의 방화벽/접근 권한에 주의합니다. `reload=True`는 개발 전용입니다.

## 3. 공통 유틸리티 — utill.py

### 환경 설정 및 CSV 읽기

```python
from pathlib import Path                  # 운영체제에 독립적인 경로 처리
import pandas as pd                       # 표 형태 데이터 처리
import traceback                          # 예외 발생 시 상세 오류 출력
from dotenv import load_dotenv            # .env 파일의 설정을 환경변수로 로드
load_dotenv()                              # 현재 .env 설정 적용
import os                                 # os.getenv()로 API 키 등 조회
from elasticsearch import Elasticsearch   # Elasticsearch 연결 클래스
es = Elasticsearch(os.getenv('ELASTIC_ENDPOINT'))  # 환경변수의 ES 서버 주소로 클라이언트 생성

def load_csv(fileName):                   # CSV 파일명을 받아 DataFrame으로 반환
    BASE_DIR = Path(__file__).resolve().parents[0]  # utill.py가 위치한 디렉터리
    DOCUMENT_FILE = BASE_DIR / 'data' / 'ml-latest-small' / fileName  # 읽을 CSV의 전체 경로
    frame = None                          # 실패했을 때 반환할 기본값
    try:                                  # 파일 읽기 중 오류에 대비
        frame = pd.read_csv(DOCUMENT_FILE) # CSV를 DataFrame으로 파싱
    except Exception as e:                # 오류가 나면 이 블록 실행
        traceback.print_exc()             # 발생 위치와 스택 출력
        print('read_csv 파일 로딩 오류', e) # 오류 메시지 출력
    return frame                          # 성공 시 DataFrame, 실패 시 None
```

실제로는 API 키/서버 주소 설정이 누락된 경우 실행 오류가 날 수 있습니다. `.env`는 공개 Git 저장소에 커밋하지 마세요.

### Gemini 임베딩

```python
def embedding_with_gemini(chunks):                 # 청크 목록을 임베딩해 ES 색인 작업 목록 생성
    api_key = os.getenv('GEMINI_API_KEY')          # 비밀 API 키를 환경변수에서 로드
    client = genai.Client(api_key=api_key)         # Gemini API 클라이언트 생성
    actions = []                                   # Elasticsearch bulk 작업을 쌓을 리스트
    for chunk in chunks:                          # 청크를 하나씩 처리
        result = client.models.embed_content(     # 텍스트를 수치 벡터로 변환하는 API 호출
            model='gemini-embedding-2',           # 원본 코드에서 선택한 임베딩 모델명
            contents=[types.Content(parts=[types.Part.from_text(text=chunk['content'])])],  # 임베딩할 텍스트
            config=types.EmbedContentConfig(output_dimensionality=768)  # 벡터 길이 768로 설정
        )
        chunk['embedding'] = result.embeddings[0].values  # 청크에 반환된 실수 벡터 저장
        actions.append({                          # bulk 색인을 위한 작업 딕셔너리 추가
            '_index': os.getenv('ES_INDEX'),      # 저장 대상 인덱스 이름
            '_id': f'{chunk["movieId"]}-{chunk["chunk_index"]}', # 영화·청크 고유 ID
            '_source': chunk                      # 실제 저장할 문서 전체
        })
        time.sleep(0.7)                           # 요청 사이 간격 확보
    return actions                                # Elasticsearch bulk용 작업 목록 반환
```

### OpenAI 임베딩 (배치 처리)

```python
def embedding_with_openai(chunks):                     # 여러 청크를 묶어서 임베딩
    api_key = os.getenv('OPENAI_API_KEY')               # 인증 키 가져오기
    client = OpenAI(api_key=api_key)                     # OpenAI API 클라이언트 생성
    actions = []                                        # ES bulk 작업 리스트
    last_index = 0                                      # 전체 chunks에서 현재 처리 위치
    time_before = time.time()                           # 배치 처리 시간 측정용 시작 시각
    contents = [chunk['content'] for chunk in chunks]   # 각 청크에서 텍스트만 뽑기
    for idx_start in range(0, len(contents), 2047):     # 최대 2047개씩 나누어 처리
        contents_part = contents[idx_start:idx_start + 2047] # 현재 API 요청에 넣을 텍스트 목록
        result = client.embeddings.create(              # 임베딩 API 호출
            model='text-embedding-3-small',             # 원본에서 선택한 모델
            input=contents_part,                        # 여러 입력을 한 번에 전달
            encoding_format='float',                    # 문자열 대신 실수 벡터 반환
            dimensions=768                              # ES 매핑과 동일한 차원 지정
        )
        vectors = [d.embedding for d in sorted(result.data, key=lambda item: item.index)] # 입력 순서와 맞춤
        for vector in vectors:                          # 반환 벡터를 차례로 순회
            chunks[last_index]['embedding'] = vector    # 원본 청크에 벡터 부착
            actions.append({                            # 인덱싱 작업 만들기
                '_index': os.getenv('ES_INDEX'),        # 대상 인덱스
                '_id': f'{chunks[last_index]["movieId"]}-{chunks[last_index]["chunk_index"]}', # 문서 ID
                '_source': chunks[last_index]           # 전체 청크 데이터 저장
            })
            last_index += 1                             # 처리한 청크만큼 이동
        time_after = time.time()                        # 배치 종료 시각
        print('걸린시간(2047개):', time_after - time_before) # 경과 시간 출력
        time_before = time.time()                       # 다음 배치 측정 준비
    return actions                                      # ES bulk 작업 리스트 반환
```

**차이:** Gemini 함수는 원본 기준 청크별로 요청하고, OpenAI 함수는 여러 청크를 한 번에 요청합니다. 임베딩은 문장의 의미를 수치로 표현하지만, **임베딩 자체가 답변을 생성하는 것은 아닙니다**.

### 검색 결과를 보기 편하게 변환

```python
def formatter(resp):                       # Elasticsearch의 복잡한 응답을 간단히 변환
    results = []                           # 가공한 검색 결과 목록
    for hit in resp['hits']['hits']:       # 실제 검색 히트마다 반복
        document = hit.get('_source', {})  # 문서 본문 가져오기 (현재 원본에서는 변수 미사용)
        results.append({                   # 결과 형태 정리
            'document': hit.get('_source', {}), # 원문 문서
            'score': hit.get('_score')     # 검색 관련도 점수
        })
    return {                               # API가 반환할 구조
        'results': results,                # 문서별 결과 목록
        'total': resp['hits']['total']['value'] # 전체 검색 건수
    }
```

## 4. 데이터 조회와 정제 — es_router.py

### /read/head · /read/valid

```python
@router.get('/read/head')                          # CSV 상위 5행을 조회할 GET 주소
def read(fileName: Literal['movies.csv', 'tags.csv', 'ratings.csv'] = 'movies.csv'): # 허용 파일 제한
    frame = utill.load_csv(fileName)               # CSV를 DataFrame으로 읽음
    if frame is None:                              # 읽기 실패 확인
        return {'ERROR': '파일을 불러오지 못했습니다'} # 오류 JSON
    preview = frame.head().astype(object).to_dict(orient='records') # 처음 5행을 JSON 직렬화하기 쉬운 형태로 변환
    return preview                                 # 데이터 리스트 반환

@router.get('/read/valid')                         # 데이터의 참조 무결성·평점 범위 확인
def valid():
    df_movies = utill.load_csv('movies.csv')       # 영화 목록
    df_tags = utill.load_csv('tags.csv')           # 영화 태그 목록
    df_ratings = utill.load_csv('ratings.csv')     # 사용자 평점 목록
    movie_ids = set(df_movies['movieId'].dropna()) # 결측값 제거 후 영화 ID의 중복 제거
    tag_ids = set(df_tags['movieId'].dropna())     # 태그 파일의 영화 ID 집합
    rating_ids = set(df_ratings['movieId'].dropna()) # 평점 파일의 영화 ID 집합
    result = {}                                    # 응답 딕셔너리
    result['no_id'] = {}                           # 존재하지 않는 영화 참조 집계
    result['no_id']['tags'] = len(tag_ids - movie_ids)  # 영화 목록에 없는 태그 movieId 개수
    result['no_id']['ratings'] = len(rating_ids - movie_ids) # 영화 목록에 없는 평점 movieId 개수
    result['rating range'] = {}                    # 평점 최소/최대 보관
    result['rating range']['min'] = float(df_ratings['rating'].min()) # 최소 평점
    result['rating range']['max'] = float(df_ratings['rating'].max()) # 최대 평점
    return result                                 # 검증 결과 반환
```

### makeContent() — 제목·장르·태그를 검색 텍스트로

```python
df_movies = utill.load_csv('movies.csv')               # 영화 메타데이터
df_tags = utill.load_csv('tags.csv')                   # 사용자 태그
result = pd.DataFrame()                                # 가공 결과를 담을 빈 표
result['movieId'] = df_movies['movieId']                # 영화별 고유 ID 복사
result['title'] = df_movies['title'].astype(str).str.strip() # 문자열 변환 후 앞뒤 공백 제거
def parse_genre(genres):                               # 장르 문자열을 배열로 바꿀 내부 함수
    result = []                                        # 반환할 장르 리스트
    if str(genres).strip() in ('', '(no genres listed)'): # 장르가 없으면
        return result                                  # 빈 리스트 반환
    list_genre = str(genres).split('|')                 # 'Action|Comedy'를 2개로 분리
    for genre in list_genre:                           # 각 장르 순회
        result.append(genre.strip().lower())            # 공백 제거+소문자 변환 후 추가
    return result                                      # 장르 리스트 반환
result['list_genre'] = df_movies['genres'].map(parse_genre) # 영화별 장르 리스트 생성
tags = df_tags[['movieId', 'tag']].copy()               # 필요한 두 열만 독립 복사
tags['tag'] = tags['tag'].astype(str).str.strip().str.lower() # 태그 표준화
tags = tags.drop_duplicates(['movieId', 'tag'])        # 같은 영화에 달린 같은 태그 제거
movie_tags = tags.groupby('movieId')['tag'].agg(list).to_dict() # 영화 ID별 태그 모아 딕셔너리 생성
result['list_tag'] = df_movies['movieId'].map(lambda id: movie_tags.get(id, [])) # 영화별 태그 조회
result['content_text'] = result.apply(                 # 각 행을 통합 검색문으로 변환
    lambda info: ' '.join(                             # 공백으로 텍스트 결합
        [info['title']] + info['list_genre'] + info['list_tag'] # 제목+장르+태그
    ).strip(),                                         # 좌우 공백 제거
    axis=1                                             # 열 방향으로 한 행씩 처리
)
return result.reset_index(drop=True)                   # 인덱스를 0부터 다시 설정해 반환
```

`map`은 보통 Series의 각 값에, `apply(axis=1)`는 DataFrame의 각 행에 함수를 적용합니다. 위 코드는 **함수 내부 핵심 구문 발췌**입니다.

### makeChunk() — 오버랩 청킹

```python
def makeChunk():                                     # 검색문을 청크 여러 개로 나누기
    size_chunk = 50                                 # 청크 최대 길이: 문자 50개
    overlap = 15                                    # 다음 청크와 겹칠 문자 수: 15개
    chunks = []                                     # 모든 청크를 담는 리스트
    dataFrame = makeContent()                       # 영화별 통합 검색문 생성
    content = dataFrame.to_dict(orient='records')   # DataFrame을 딕셔너리 리스트로 변환
    step = size_chunk - overlap                     # 다음 시작 위치: 35글자 뒤
    for idx_content, info in enumerate(content):   # 영화를 하나씩 읽고 행 번호도 보관
        text = info.get('content_text', '').strip() # 검색할 문자열을 추출
        if not text:                                # 빈 문자열이면
            continue                               # 이번 영화는 건너뛰기
        for idx, idx_start in enumerate(range(0, len(text), step)): # 35글자 간격으로 이동
            chunk = text[idx_start:idx_start + size_chunk] # 최대 50글자 분리
            if chunk:                               # 문자열이 비어 있지 않으면
                chunks.append({                     # 청크 메타데이터와 본문을 저장
                    'index': idx_content,           # 원본 영화 행 위치
                    'movieId': int(info['movieId']), # 원본 영화 ID
                    'title': str(info['title']),    # 영화 제목
                    'genres': list(info['list_genre']), # 장르 리스트
                    'tags': list(info['list_tag']), # 태그 리스트
                    'content': chunk,               # 실제 청크 텍스트
                    'chunk_index': idx              # 같은 영화의 청크 순번
                })
    return chunks                                   # 청크 목록 반환
```

**주의:** 문자 단위 분할이므로 단어 중간에서 끊길 수 있습니다. 토큰 단위 청킹과는 다릅니다.

## 5. Elasticsearch 인덱싱과 검색

### /es/bulk

```python
@router.post('/es/bulk')                           # 문서를 Elasticsearch에 일괄 저장할 POST API
def bulk():
    target = makeChunk()                           # 영화 검색문을 청크로 만들기
    actions = utill.embedding_with_openai(target)  # 768차원 벡터와 bulk 작업 생성
    if not utill.es.indices.exists(index=os.getenv('ES_INDEX')): # 인덱스 존재 확인
        mappings = {'properties': {                 # ES 필드 타입(매핑) 정의
            'index': {'type': 'integer'},           # 행 위치는 정수
            'movieId': {'type': 'integer'},         # 영화 ID는 정수
            'title': {'type': 'text'},              # 제목은 전문 검색
            'genres': {'type': 'keyword'},          # 장르는 정확 일치/필터용
            'tags': {'type': 'text'},                # 태그 전문 검색
            'content': {'type': 'text'},             # 청크 전문 검색
            'chunk_index': {'type': 'integer'},     # 청크 번호
            'embedding': {'type': 'dense_vector', 'dims': 768} # 의미 검색용 벡터
        }}
        utill.es.indices.create(index=os.getenv('ES_INDEX'), mappings=mappings) # 인덱스 생성
    success, errors = helpers.bulk(                 # 여러 건을 한 번에 색인
        utill.es, actions, stats_only=False, raise_on_error=False # 오류 문서를 수집해 반환
    )
    return {'msg': {'succ': success, 'errors': errors}} # 저장 결과 반환
```

현재 함수는 **인덱스 존재 여부를 확인하기 전에** 임베딩을 생성합니다. 외부 API 호출 비용·지연이 생길 수 있고 인덱스 매핑이 다른 기존 인덱스에서는 차원 충돌에 주의해야 합니다.

### 키워드 검색 · 벡터 검색

```python
def search_movies(keyword: str, size: int = 10):           # BM25 기반 검색 함수를 감싼 helper
    response = utill.es.search(                            # Elasticsearch 검색 요청
        index=os.getenv('ES_INDEX'),                       # 조회 대상 인덱스
        query={'multi_match': {                            # 여러 텍스트 필드에 걸친 검색
            'query': keyword,                              # 사용자가 입력한 검색어
            'fields': ['title^4', 'genres', 'tags^2', 'content^3'] # 제목 4배, 태그 2배, 본문 3배 가중치
        }},
        size=size                                          # 가져올 검색 결과 수
    )
    return response                                       # ES 원본 응답 반환

def search_vector(keyword: str, size: int = 10):          # 자연어 의미 유사도 검색
    querys = [{'content': keyword, 'movieId': 0, 'chunk_index': 0}] # 기존 Gemini 유틸 입력 형태에 맞추기
    vectors = utill.embedding_with_gemini(querys)         # 검색어를 임베딩하고 bulk 액션 형태로 받기
    vector = vectors[0]['_source']['embedding']            # 벡터 숫자 리스트만 추출
    response = utill.es.search(                            # 벡터 최근접 이웃 검색
        index=os.getenv('ES_INDEX'),                       # 인덱스 선택
        knn={'field': 'embedding',                          # 검색할 벡터 필드
             'query_vector': vector,                       # 검색어 벡터
             'num_candidates': max(size * 10, 50),         # 탐색 후보 수
             'k': size},                                  # 반환할 최근접 이웃 수
        size=size                                          # 최종 응답 크기
    )
    return response                                       # KNN 결과 반환
```

**중요한 호환성 이슈:** `/es/bulk`는 **OpenAI**로 문서를 임베딩하지만 `search_vector()`는 **Gemini**로 질의를 임베딩합니다. 벡터 차원이 둘 다 768이어도 모델의 좌표 공간은 달라서 의미 유사도 결과를 신뢰할 수 없습니다. 같은 모델로 **문서와 질문을 모두 임베딩**해야 합니다. 또한 현재 `search_vector`를 직접 호출하는 HTTP 엔드포인트는 보이지 않습니다.

### terms 검색

```python
def term_movieId(ids: list):                           # 여러 movieId를 정확 일치 검색
    response = utill.es.search(                       # ES 쿼리 수행
        index=os.getenv('ES_INDEX'),                   # 대상 인덱스
        query={'terms': {'movieId': [int(i) for i in ids]}}, # SQL의 IN과 비슷한 조건
        size=len(ids) * 5                              # 한 영화에 여러 청크가 있다고 가정한 크기
    )
    return response                                    # 검색 결과 반환

@router.get('/es/select/terms')                       # URL에서 ids 쿼리 파라미터 반복 수신
def terms(ids: list[int] = Query(...)):               # 예: ?ids=1&ids=2
    response = term_movieId(ids)                      # ID 목록 조회
    return {'msg': utill.formatter(response)}         # API 응답으로 변환
```

청크 수가 영화별로 5개를 넘으면 `size=len(ids)*5`로 **모든 매칭 문서를 보장하지 않습니다**.

## 6. CBF — 콘텐츠 기반 추천

```python
def content_based_filtering(list_movieid: list, candidate_size: int = 10): # 좋아한 영화 ID들을 입력
    selected = term_movieId(list_movieid)               # 좋아한 영화들의 색인된 문서 검색
    genre_counter = Counter()                           # 장르 등장 횟수 보관
    tag_counter = Counter()                             # 태그 등장 횟수 보관
    for hit in selected['hits']['hits']:                # ES 검색 결과 반복
        source = hit['_source']                          # 해당 영화/청크 문서
        genre_counter.update(source.get('genres', []))  # 장르 빈도 합산
        tag_counter.update(source.get('tags', []))      # 태그 빈도 합산
    top_n = 5                                          # 상위 5개 특징 선택
    terms_genre = [term for term, count in genre_counter.most_common(top_n)] # 많이 등장한 장르
    terms_tag = [term for term, count in tag_counter.most_common(top_n)] # 많이 등장한 태그
    terms = []                                         # 검색 조건 목록
    terms.extend(terms_genre)                          # 장르 추가
    terms.extend(terms_tag)                            # 태그 추가
    query = ' '.join(dict.fromkeys(terms))              # 기존 순서를 지키며 중복 제거
    response = search_movies(query, candidate_size)    # 장르·태그를 검색어로 추천 후보 검색
    return response['hits']['hits']                     # 추천 후보 반환
```

**주의:** 영화가 여러 청크로 저장되어 같은 장르/태그를 여러 번 집계할 수 있고, 반환 결과에서도 **이미 본 영화가 자동 제외되지는 않습니다**. CBF 후보의 원래 순위가 하이브리드에서 중요합니다.

## 7. CF — 협업 필터링과 데이터 누수 방지

### split_train_test()

```python
def split_train_test(test_size: float = 0.2):           # 각 사용자의 최신 평점을 평가 데이터로 분리
    if not 0 < test_size < 1:                           # 0~1 사이인지 확인
        raise ValueError('test_size는 0과 1 사이여야 합니다.') # 잘못된 입력이면 중단
    frame_ratings = utill.load_csv('ratings.csv')        # MovieLens 평점 파일 읽기
    data = frame_ratings.copy()                         # 원본 수정 방지
    data['original_order'] = range(len(data))           # 원래 행 순서 기록
    data['timestamp'] = pd.to_numeric(data['timestamp'], errors='coerce') # 시간을 숫자로 변환
    valid_data = data[data['timestamp'].notna()].copy() # 유효한 시간의 데이터만
    no_time = data[data['timestamp'].isna()].copy()     # 시간 없는 데이터는 별도 보관
    test_indices = []                                  # 테스트로 보낼 행 인덱스
    for _, group in valid_data.groupby('userId', sort=False): # 사용자별 평점 묶기
        if len(group) <= 1:                            # 평점 한 개면 학습에 남김
            continue                                   # 평가에 포함하지 않음
        ordered = group.sort_values(['timestamp', 'original_order'], kind='stable') # 시간 순 정렬
        test_counter = min(len(ordered) - 1, max(1, math.ceil(len(ordered) * test_size))) # 최소 1개 테스트·학습 확보
        test_indices.extend(ordered.tail(test_counter).index.tolist()) # 마지막(최신) 행 저장
    test = valid_data.loc[test_indices].copy()         # 정답(평가) 평점 데이터
    train = valid_data.drop(index=test_indices)       # 테스트 데이터를 뺀 과거 기록
    train = pd.concat([train, no_time])                # 날짜 없는 평점은 학습에만 추가
    test = test.sort_values('original_order', kind='stable').drop(columns='original_order') # 원본 순서 복원
    train = train.sort_values('original_order', kind='stable').drop(columns='original_order') # 보조 열 삭제
    return test.reset_index(drop=True), train.reset_index(drop=True) # 원본 코드의 반환 순서는 (test, train)
```

**반환 순서를 꼭 기억:** 보통 `train, test`라고 쓰기 쉽지만 **이 코드의 실제 반환값은 `test, train`** 입니다.

### collaborative_filtering()

```python
def collaborative_filtering(userId, top_k=10):            # 특정 사용자에게 영화 추천
    test, train = split_train_test()                     # 과거/미래 평점 분리
    data = train[['userId', 'movieId', 'rating']].copy()  # 모델에 필요한 열만 선택
    if userId not in data['userId'].values:              # 학습 데이터에 사용자 존재 여부 확인
        raise ValueError(f'{userId}을/를 찾을 수 없습니다.') # 없으면 예외
    reader = Reader(rating_scale=(0.5, 5.0))             # 평점 척도 정의
    data_set = Dataset.load_from_df(data[['userId', 'movieId', 'rating']], reader) # Surprise 형식 변환
    train_set = data_set.build_full_trainset()           # Surprise 학습용 구조 생성
    model = KNNWithMeans(                                # 평균 평점 보정 KNN 모델
        k=30,                                            # 최대 30명 유사 이웃 활용
        sim_options={'name': 'pearson', 'user_based': True}, # 사용자 기반 피어슨 상관계수
        verbose=False                                    # 학습 로그 최소화
    )
    model.fit(train_set)                                 # 유사도 모델 학습
    inner_user_id = train_set.to_inner_uid(userId)       # 외부 userId를 내부 번호로 변환
    rated_movie = set()                                  # 이미 평가한 영화 ID
    for inner_movie_id, rating in train_set.ur[inner_user_id]: # 사용자가 남긴 평점 내역
        rated_movie.add(train_set.to_raw_iid(inner_movie_id)) # 원래 movieId로 변환해 추가
    candidate_movies = [                                 # 학습 데이터에 있으나 안 본 영화 선택
        train_set.to_raw_iid(mid)                        # 내부 ID를 외부 ID로 바꿈
        for mid in range(train_set.n_items)              # 모든 학습 영화 반복
        if train_set.to_raw_iid(mid) not in rated_movie  # 이미 본 학습 영화 제외
    ]
    recommend = []                                       # 영화별 예상 평점
    for movieId in candidate_movies:                     # 모든 추천 후보에 대해
        score = model.predict(userId, movieId).est       # 사용자에게 예측되는 별점
        recommend.append({'movieId': movieId, 'score': score}) # 결과 적재
    recommend.sort(key=lambda x: x['score'], reverse=True) # 예측 평점 내림차순 정렬
    return recommend[:top_k]                             # 상위 k개 반환
```

여기에서 CF는 '같은 장르라서'가 아니라 **평점 패턴이 비슷한 사용자**를 바탕으로 추천합니다. 원본 `requirements.txt`에 `surprise` 관련 의존성 선언이 없어 별도 설치가 필요할 수 있습니다.

### recall_at_k() — 추천 성능 평가

```python
def recall_at_k(userId, test, recommend, threshold=4.0, k=10):  # 모델의 정답 회수율 계산
    relevant_movies = set(test.loc[                      # 테스트 평점 중 진짜 좋아한 영화 ID 집합
        (test['userId'] == userId) & (test['rating'] >= threshold), # 특정 사용자·기준 평점 이상
        'movieId'                                       # ID 열만 선택
    ])
    if len(relevant_movies) == 0:                       # 평가할 정답이 없다면
        return -1.0                                     # 원본의 평가 불가 표시값
    recommend_movies = {item['movieId'] for item in recommend[:k]} # 상위 k개 추천 영화
    hit_count = len(relevant_movies & recommend_movies) # 추천 결과와 정답의 교집합 수
    result = hit_count / len(relevant_movies)           # Recall@K = 맞힌 정답 수 / 전체 정답 수
    return result                                       # 0~1 사이 회수율
```

**오해 주의:** Recall의 분모는 *전체 추천 개수*가 아니라 *전체 실제 정답 개수*입니다. 예를 들어 진짜 좋아한 영화가 5개이고 상위 10개 추천 중 2개가 정답이면 `Recall@10 = 2/5 = 0.4`입니다. 원본 `/recommend/recall`은 `threshold=2.0`, `k=50`으로 호출합니다.

## 8. CBF + CF 결합 — hybrid_filtering()

### 지금 실제 코드가 하는 일

```python
response_cbf = content_based_filtering(list_movieId, candidate_size) # 콘텐츠 추천 후보
result_cbf = set()                               # CBF 영화 ID의 중복 제거 집합
for hit in response_cbf:                         # ES hit를 순회
    movieId = int(hit['_source']['movieId'])     # movieId 추출
    if movieId not in list_movieId:              # 사용자가 입력한 좋아한 영화는 제외
        result_cbf.add(movieId)                  # 집합에 영화 ID 추가
response_cf = collaborative_filtering(userId, candidate_size) # 협업 추천 후보
result_cf = set()                                # CF 영화 ID 집합
for hit in response_cf:                          # 예측 평점 순으로 나온 결과를 순회
    movieId = hit.get('movieId')                 # 영화 ID 추출
    if movieId not in list_movieId:              # 이미 입력한 영화 제외
        result_cf.add(movieId)                  # 집합에 보관
rrf_score = {}                                   # 영화별 RRF 누적 점수
rank_constant = 60                              # 상위 순위의 영향을 완화하는 상수
for rank, movieId in enumerate(result_cbf, start=1): # CBF 후보를 순회
    if rrf_score.get('movieId'):                 # ⚠ 잘못된 조건: 실제 movieId 변수 대신 문자열 키를 확인
        rrf_score[movieId] += 1/(rank_constant+rank) # 점수 누적(현재 분기 거의 진입 안 함)
    else:
        rrf_score[movieId] = 1/(rank_constant+rank) # 새 점수 대입
for rank, movieId in enumerate(result_cf, start=1): # CF 후보 순회
    if rrf_score.get('movieId'):                 # ⚠ 동일한 잘못된 문자열 키
        rrf_score[movieId] += 1/(rank_constant+rank) # 기존 점수 누적 의도
    else:
        rrf_score[movieId] = 1/(rank_constant+rank) # 기존 CBF 점수를 덮어쓸 수 있음
result = sorted(rrf_score.items(), key=lambda x: x[1], reverse=True) # 점수 내림차순
return result[:top_k]                            # 영화 ID·RRF 점수 튜플 상위 k개
```

**문제 1 — 핵심 버그:** `rrf_score.get('movieId')`는 문자열 `'movieId'` 키만 검사합니다. 실제 ID를 검사하려면 `if movieId in rrf_score:` 또는 `rrf_score.get(movieId)`를 써야 합니다.

**문제 2 — 순위 소실:** `set()`에는 **검색 결과 순서가 보장되지 않습니다**. RRF는 '몇 번째로 추천됐는지'가 생명이므로 후보별 중복만 제거하되 순서를 유지해야 합니다.

**문제 3 — 중복 청크:** CBF는 같은 영화의 서로 다른 청크를 반환할 수 있으므로 최초 등장한 영화만 남기는 방식이 적절합니다.

### 수정 아이디어 (학습용 대안, 원본 미수정)

```python
def combine_rrf(response_cbf, response_cf, excluded_ids, top_k=10): # 이미 검색된 후보를 안전하게 합산
    excluded_ids = set(excluded_ids)                  # 제외할 영화 ID를 집합으로
    cbf_ids = list(dict.fromkeys(                     # CBF 등장 순서를 지키며 중복 제거
        int(hit['_source']['movieId']) for hit in response_cbf
        if int(hit['_source']['movieId']) not in excluded_ids
    ))
    cf_ids = list(dict.fromkeys(                      # CF도 원래 점수 순서 유지
        int(item['movieId']) for item in response_cf
        if int(item['movieId']) not in excluded_ids
    ))
    rrf_score = {}                                    # 영화별 누적 점수
    rank_constant = 60                                # RRF 안정화 상수
    for ranking in (cbf_ids, cf_ids):                 # 각 추천 결과를 차례대로 합산
        for rank, movie_id in enumerate(ranking, start=1): # 1위부터 순위 부여
            rrf_score[movie_id] = rrf_score.get(movie_id, 0) + 1 / (rank_constant + rank) # 점수 누적
    return sorted(rrf_score.items(), key=lambda x: x[1], reverse=True)[:top_k] # 최종 상위 k개
```

**RRF 식:** `score(movie) = Σ 1 / (60 + rank_in_each_list)`. 같은 영화가 CBF와 CF 양쪽에서 상위에 나오면 점수가 합산됩니다.

### /recommend/hybrid의 추가 확인사항

- `score = i[1],`의 **끝 쉼표** 때문에 수치가 아니라 원소 1개짜리 튜플이 됩니다. `score = i[1]`로 수정해야 의도한 숫자가 됩니다.
- `df_movies.loc[...,'title'].iloc[0]`은 영화 ID가 없으면 `IndexError`를 낼 수 있습니다.
- 추천 요청마다 `split_train_test()` 및 CF 모델 전체 재학습을 실행하므로 호출 비용이 큽니다. 실제 서비스라면 모델/학습 결과 캐싱을 검토합니다.
- `Counter.update(food)`에 문자열을 직접 넘기면 단어가 아닌 **글자별 빈도**를 셉니다. 음식 이름 단위로 집계하려면 `Counter.update([food])`를 써야 합니다.
- 이 문서는 분석과 설명이 목적이며 기존 Python 버그를 자동 수정하거나 테스트 통과를 보장하지 않습니다.

## 9. 사용 가능한 주요 API 요약

| 메서드 | 주소 | 역할 |
|---|---|---|
| GET | `/` | Hello World |
| GET | `/read/head` | CSV 상위 5행 |
| GET | `/read/valid` | MovieLens 무결성 확인 |
| GET | `/make/content` | 통합 검색 텍스트 미리보기 |
| GET | `/make/chunk` | 청크 상위 10개 |
| GET | `/make/embedding/gemini` | Gemini 임베딩 샘플 |
| GET | `/make/embedding/openai` | OpenAI 임베딩 샘플 |
| GET | `/es/health` | ES 연결 ping |
| POST | `/es/bulk` | 전체 청크 임베딩·색인 (비용/시간 주의) |
| GET | `/es/select/multi_match` | 키워드 검색 |
| GET | `/es/select/terms` | movieId 목록 검색 |
| GET | `/recommend/test/counter` | Counter 실습 |
| GET | `/recommend/cbf` | 콘텐츠 기반 후보 추천 |
| GET | `/es/recommend/cf` | 협업 필터링 |
| GET | `/recommend/recall` | Recall@K 평가 |
| GET | `/recommend/hybrid` | 결합 추천 (현재 버그 있음) |

## 10. 공부 순서와 연습 문제

1. **Pandas**: `head`, `dropna`, `astype`, `groupby`, `agg(list)`, `apply(axis=1)` 실습.
2. **FastAPI**: `@router.get`, `Query(...)`, `include_router`의 흐름 설명하기.
3. **검색 준비**: `makeContent → makeChunk → embedding` 데이터 형태를 직접 출력해 비교.
4. **Elasticsearch**: `keyword/text/dense_vector` 차이와 `multi_match`, `terms`, `knn` 비교.
5. **CBF/CF**: 장르·태그 기반 추천과 사용자 평점 기반 추천의 입력·출력 비교.
6. **검증**: 최신 평점을 학습에서 제외하는 이유, Recall@K 분자·분모 설명.
7. **디버깅**: 하이브리드에서 `set` → 순서 보존, `get('movieId')` → `get(movieId)`, 쉼표 튜플 버그 수정.
8. **추가 학습**: LangGraph 자체를 배우려면 `StateGraph`, 상태(State), 노드, 엣지, 조건 분기를 별도 예제로 구현해 보세요.

## 11. 학습 체크리스트

- [ ] 데이터프레임과 Series 차이를 말할 수 있다
- [ ] 청킹 오버랩(50/15)의 의미를 설명할 수 있다
- [ ] 문서와 질의를 같은 임베딩 모델로 처리해야 하는 이유를 안다
- [ ] Elasticsearch 검색 결과의 `_source`와 `_score`를 구분한다
- [ ] CBF와 CF 차이를 예시로 설명할 수 있다
- [ ] Surprise의 user-based KNN 흐름을 말할 수 있다
- [ ] 시간 순 평가 분리와 Recall@K 계산을 설명할 수 있다
- [ ] RRF에서 순서를 보존해야 하는 이유를 안다
- [ ] 현재 하이브리드 구현의 버그 세 가지를 찾아 수정할 수 있다

---

**정리:** 이 폴더는 단순한 'LangGraph 강의'라기보다, **실제 검색·추천 백엔드를 만들면서 Pandas→임베딩→Elasticsearch→CBF/CF→RRF→모델 평가를 연결하는 실습**입니다. 문서의 코드는 교육 목적으로 요약·주석화했으며 실행 가능한 수정본을 의미하지 않습니다.
