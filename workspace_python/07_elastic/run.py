
# dotenv 사용법
from dotenv import load_dotenv
load_dotenv()

import os
key1=os.getenv('key1')
key2=os.getenv('key2')
key3=os.getenv('key3')

print('key1',key1)
print('key2',key2)
print('key3',key3)

# if not key3:
#     raise ValueError('key3 환경 변수가 없습니다. .env 파일 확인요먕')

from config import ELASTIC_ENDPOINT,ELASTIC_API_KEY
from elasticsearch import Elasticsearch

es=Elasticsearch(
    ELASTIC_ENDPOINT,
    api_key=ELASTIC_API_KEY
)

connected=es.ping()
print('엘라스틱 서치 연결상태', connected)