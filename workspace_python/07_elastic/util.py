import os
import json

from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from pathlib import Path

# .env 파일 읽기
load_dotenv()

# .env에 저장된 값 가져오기
ELASTIC_ENDPOINT = os.getenv("ELASTIC_ENDPOINT")
ELASTIC_API_KEY = os.getenv("ELASTIC_API_KEY")

# Elasticsearch 연결
es = Elasticsearch(
    ELASTIC_ENDPOINT,
    api_key=ELASTIC_API_KEY
)


def load_documents():
    BASE_DIR = Path(__file__).resolve().parents[1]
    DOCUMENT_FILE = BASE_DIR / 'data' / 'data.json'

    result = {}

    try:
        with open(DOCUMENT_FILE, 'r', encoding='utf-8') as file:
            result = json.load(file)
            print(result)

    except Exception as e:
        print('open 하다가 오류 발생 :', e)

    return result