# 📚 Human Education Center | 개발 학습 기록

> **HTML/CSS 기초부터 JavaScript, Python, FastAPI, 데이터베이스, 검색·AI 실습까지**  
> 휴먼교육센터에서 공부하면서 작성한 예제, 과제, 실습 코드와 팀 프로젝트를 모아 둔 학습 저장소입니다.

[![GitHub](https://img.shields.io/badge/GitHub-Learning%20Repository-181717?logo=github)](https://github.com/doyoung1011/Humancenter)
![HTML](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)

## 📌 저장소 소개

이 저장소는 완성된 하나의 서비스가 아니라 **배우는 과정 자체를 기록한 실습 아카이브**입니다.

- 수업에서 배운 문법과 개념을 직접 작성한 코드로 복습했습니다.
- 단순 예제에서 화면 구현, API·DB 연동, 팀 프로젝트로 학습 범위를 확장했습니다.
- 일부 수업 내용은 커밋이 누락되어 있거나 파일이 중간 단계에 머물러 있습니다.
- 따라서 아래 정리는 **현재 저장소에 남아 있는 파일을 기준으로 한 학습 내용**이며, 모든 예제가 완성되거나 실행 검증된 것은 아닙니다.

## 🧭 학습 내용 한눈에 보기

| 영역 | 주요 학습 내용 | 코드 위치 |
| --- | --- | --- |
| HTML | 태그, 목록, 표, 이미지, 링크, 폼, 페이지 구조 | [WorkSpace_Html](./WorkSpace_Html) |
| CSS | 선택자, 단위, 박스 모델, display, position, flex, 반응형, 애니메이션 | [WorkSpace_Html/css](./WorkSpace_Html/css) |
| JavaScript | 변수, 연산자, 조건·반복문, 배열, 함수, DOM, 이벤트, JSON, AJAX | [javascript](./javascript) |
| Python 기초 | 자료형, 제어문, 함수, 파일, 클래스, 상속, 예외, 모듈 | [workspace_python](./workspace_python) |
| 웹 백엔드 | FastAPI 라우팅, 요청·응답, Jinja2, CRUD 실습 | [workspace_python/todos](./workspace_python/todos) |
| 데이터베이스 | SQL, PyMySQL, SQLModel, DTO, 세션 및 DB 연동 | [03_database](./workspace_python/03_database) |
| 웹 상태·파일 | 업로드, 쿠키, 세션 | [04_fileupload](./workspace_python/04_fileupload), [05_cookie_session](./workspace_python/05_cookie_session) |
| 팀 프로젝트 | 맛집 정보·리뷰·회원 기능 중심 웹 서비스 | [Team](./workspace_python/Team) |
| 데이터 분석·ML | Pandas, 전처리, 데이터 분할, RandomForest, 평가 지표 | [06_scikit_learn](./workspace_python/06_scikit_learn) |
| 검색·임베딩 | Elasticsearch, 인덱스·매핑, 텍스트 청킹, 벡터 임베딩 | [07_elastic](./workspace_python/07_elastic) |
| 검색·추천 실습 | 영화 CSV 처리, 데이터 검증, 추천 관련 실험, LangGraph 관련 의존성 | [08_langgraph](./workspace_python/08_langgraph) |

> 위 표는 디렉터리명만으로 추정하지 않고 대표 코드 및 파일 목록을 확인해 작성했습니다. 특히 `08_langgraph`에 있는 모든 기능이 LangGraph로 구현되었다는 뜻은 아닙니다.

## 🛠️ 단계별 학습 내용

### 01. HTML · CSS — 정적인 웹 화면 만들기

**학습 주제**
- HTML 기본 구조, 다양한 태그, 목록(`ul`), 표(`table`), 이미지(`img`), 폼(`form`)
- CSS 선택자와 크기 단위, 박스 모델, `display`, `position`, `overflow`
- `flex`, 미디어 쿼리를 이용한 레이아웃 및 반응형 화면
- `transform`, `transition`, 그림자 등 시각 효과
- 기존 웹사이트 화면을 참고한 클론·레이아웃 실습

**대표 파일**
- [HTML 폼](./WorkSpace_Html/07_Form.html)
- [CSS 선택자](./WorkSpace_Html/css/01_Selector.html)
- [Flexbox](./WorkSpace_Html/css/15_flex.html)
- [반응형 미디어 쿼리](./WorkSpace_Html/css/14_media.html)
- [채팅 UI 실습](./WorkSpace_Html/실습/Chat.html)

**핵심 정리:** HTML은 문서의 구조, CSS는 표현과 배치를 담당합니다. 같은 화면이라도 요소를 어떻게 그룹화하고 배치하는지가 유지보수에 중요하다는 점을 실습했습니다.

### 02. JavaScript — 동적인 화면과 사용자 상호작용

**학습 주제**
- `let`, `const`, 연산자, `if`, `for`, `while`
- 배열과 문자열, 날짜, 일반 함수와 화살표 함수
- DOM 탐색·수정, 폼 입력값 처리, 이벤트 리스너
- `map`, JSON, 비동기 요청과 AJAX
- 간단한 To-do List, 피자 주문 등 응용 예제

**대표 파일**
- [조건문](./javascript/03_if.html) · [반복문](./javascript/04_for.html) · [배열](./javascript/06_array.html)
- [함수](./javascript/08_function.html) · [DOM](./javascript/11_dom.html)
- [이벤트](./javascript/15_event.html) · [JSON](./javascript/19_json.html) · [AJAX](./javascript/20_ajax.html)
- [To-do List](./javascript/Todolist.html)

**핵심 정리:** 사용자 입력 → 이벤트 발생 → JavaScript 실행 → DOM 갱신이라는 흐름을 익히고, 서버와 데이터를 주고받는 기초를 실습했습니다.

### 03. Python — 백엔드 개발을 위한 언어 기초

**학습 주제**
- 변수, 문자열, 리스트·튜플·딕셔너리 등 컬렉션
- 조건·반복문과 문제 풀이
- 함수, 파일 입출력, 클래스·상속, 예외 처리, 모듈
- 작은 알고리즘 및 콘솔 프로그램 작성

**대표 파일**
- [기본 문법](./workspace_python/01_hello.py)
- [반복문](./workspace_python/09_for.py) · [함수](./workspace_python/11_fn.py)
- [클래스](./workspace_python/12_class.py) · [상속](./workspace_python/13_상속.py)
- [예외 처리](./workspace_python/14_try.py)

**핵심 정리:** 데이터를 변수와 자료구조에 담고, 조건·반복문·함수를 조합해 처리하는 프로그램 흐름을 학습했습니다.

### 04. FastAPI · Jinja2 — 서버와 화면 연결

**학습 주제**
- FastAPI의 `GET` 등 HTTP 라우팅과 요청·응답
- 라우터 분리 및 경로 매개변수
- Jinja2를 이용한 HTML 템플릿 렌더링
- 게시글·할 일 목록의 CRUD 흐름 실습
- 폼 데이터, 리다이렉트, 상태 관리 관련 기초 실습

**대표 폴더**
- [라우터·CRUD](./workspace_python/todos/01_router)
- [Jinja2](./workspace_python/todos/02_jinja)
- [응답 처리](./workspace_python/todos/03_response)
- [To-do CRUD 실습](./workspace_python/todos/04_todo)
- [파일 업로드](./workspace_python/04_fileupload)
- [쿠키와 세션](./workspace_python/05_cookie_session)

**핵심 정리:** 브라우저의 요청을 서버 라우터가 받고, 필요한 데이터를 처리한 뒤 JSON·HTML·리다이렉트 등의 응답을 돌려주는 구조를 학습했습니다.

### 05. SQL · 데이터베이스 — 데이터 저장과 조회

**학습 주제**
- 관계형 데이터베이스와 SQL 기초
- PyMySQL을 활용한 데이터베이스 연결
- SQLModel과 SQLAlchemy 기반 DB 작업
- DTO 모델을 통한 데이터 표현
- DB 세션, 조회·수정, `commit`·`rollback` 기초

**대표 파일**
- [PyMySQL](./workspace_python/03_database/01_pymysql.py)
- [SQLModel 실습](./workspace_python/03_database/02_sqlmodel.py)
- [사원 데이터 실습](./workspace_python/03_database/03_emp.py)
- [DTO](./workspace_python/03_database/DTO)

**핵심 정리:** 화면의 데이터가 실제 DB 테이블에 어떻게 저장되는지, API → DB 쿼리 → 응답으로 이어지는 과정을 연습했습니다.

### 06. 팀 프로젝트 — 배운 기술을 하나의 웹 서비스로 연결

[📂 팀 프로젝트 코드](./workspace_python/Team) · [📄 팀 프로젝트 README](./workspace_python/Team/README.md)

**주제:** 맛집 정보, 리뷰와 북마크 등을 중심으로 한 웹 서비스

- HTML·CSS·JavaScript·Jinja2 기반 화면
- Python·FastAPI 기반 서버
- 회원가입·로그인·마이페이지 등 회원 관련 흐름
- 맛집 정보, 리뷰·게시판·북마크 관련 화면 및 데이터 모델
- 기능별 코드 구성과 Git을 이용한 협업 경험

여기서는 개별 문법을 넘어 **화면·라우터·데이터베이스가 연결되는 전체 웹 서비스 구조**를 경험했습니다. 세부 기능의 실제 완성 여부와 담당 범위는 팀 프로젝트 문서 및 각 구현 코드를 참고해 주세요.

### 07. Pandas · 머신러닝 — 데이터 전처리와 모델 평가

[📂 scikit-learn 실습](./workspace_python/06_scikit_learn)

와인 품질 CSV 데이터를 기반으로 다음 과정을 연습했습니다.

1. `pandas.read_csv()`로 데이터 로딩 및 `head()`, `shape`, `info()`로 확인
2. 와인 품질 점수를 기준으로 이진 분류용 정답 데이터 생성
3. 입력 특성(`X`)과 정답(`y`) 분리
4. `train_test_split()`으로 학습·테스트 데이터 분할
5. `RandomForestClassifier`로 모델 학습과 예측
6. F1-score, ROC-AUC로 성능 평가

**핵심 정리:** 학습 데이터를 잘 나누는 이유와 전처리, 예측, 평가 지표의 역할을 코드로 확인했습니다.

### 08. Elasticsearch · 임베딩 — 키워드에서 의미 기반 검색으로

[📂 Elasticsearch 실습](./workspace_python/07_elastic) · [📂 추가 검색/추천 실습](./workspace_python/08_langgraph)

**학습 주제**
- Elasticsearch 인덱스 생성과 필드 매핑
- 문서 저장·조회, 텍스트 필드와 `keyword` 필드의 차이
- 정규표현식 기반 문장 분리
- 텍스트 청킹(chunking)과 오버랩(overlap)
- 벡터 임베딩(`dense_vector`)을 이용한 검색 실습
- 영화 데이터의 CSV 로딩·정제 및 추천 관련 실험

**대표 파일**
- [임베딩 라우터](./workspace_python/07_elastic/router/embedding_router.py)
- [검색 관련 라우터](./workspace_python/07_elastic/router/es_router.py)
- [영화 데이터 처리·검색 실습](./workspace_python/08_langgraph/router/es_router.py)
- [관련 의존성](./workspace_python/08_langgraph/requirements.txt)

**핵심 정리:** 키워드로 일치하는 문서를 찾는 방식과 텍스트를 벡터로 바꾸어 유사한 내용을 찾는 방식의 차이를 이해하고, 데이터 가공 → 인덱싱 → 검색의 기본 흐름을 실습했습니다.

## 📂 주요 디렉터리

```text
Humancenter/
├── WorkSpace_Html/             # HTML/CSS 기본 및 화면 실습
├── javascript/                 # JavaScript 문법, DOM, 이벤트, AJAX
├── workspace_python/
│   ├── 01_hello.py ~ 15_module.py  # Python 기초 예제
│   ├── todos/                  # FastAPI, 라우팅, Jinja2, CRUD
│   ├── 03_database/            # SQL, PyMySQL, SQLModel
│   ├── 04_fileupload/          # 파일 업로드
│   ├── 05_cookie_session/      # 쿠키·세션
│   ├── Team/                   # 맛집 웹 서비스 팀 프로젝트
│   ├── Team2/                  # 별도 보관된 팀 프로젝트 코드
│   ├── 06_scikit_learn/        # Pandas와 머신러닝
│   ├── 07_elastic/             # Elasticsearch와 임베딩
│   └── 08_langgraph/           # 영화 데이터·검색·추천 실습
├── templates/                  # 기타 HTML 템플릿
├── static/                     # 기타 정적 파일
├── api.py                      # 별도 API 실습
└── README.md
```

## 💡 공부하면서 정리한 핵심 개념

| 개념 | 이해한 내용 |
| --- | --- |
| DOM | JavaScript로 HTML 요소를 찾아 값을 읽거나 화면을 변경하는 객체 모델 |
| 비동기 통신 | 페이지 전체를 새로고침하지 않고 서버와 데이터를 주고받는 방식 |
| CRUD | 생성(Create), 조회(Read), 수정(Update), 삭제(Delete) |
| DTO | 프로그램에서 전달하거나 다룰 데이터를 구조화한 객체 |
| 세션 | 사용자별 상태를 서버 측에서 유지하는 방법 |
| 트랜잭션 | 여러 DB 작업을 하나의 논리적인 처리 단위로 다루는 것 |
| DataFrame | Pandas에서 표 형태의 데이터를 다루는 2차원 구조 |
| 임베딩 | 텍스트 등의 의미적 특징을 숫자 벡터로 표현하는 것 |
| 청킹 | 긴 문서를 검색·처리에 적합한 작은 단위로 나누는 것 |

## 📝 기록 상태와 앞으로의 보완 사항

이 저장소는 **학습 중 시행착오를 보관하는 공간**이기 때문에 아래 사항이 존재할 수 있습니다.

- 강의 내용 중 일부가 커밋되지 않아 중간 단계가 비어 있음
- 일부 코드는 작성 중인 실습본이므로 실행 오류나 미완성 기능이 남아 있을 수 있음
- 폴더별 실행 환경, 패키지 버전, 환경 변수가 서로 다를 수 있음
- 팀 프로젝트 및 개별 예제가 하나의 실행 가능한 앱으로 통합되어 있지는 않음

**추후 개선 계획**
- [ ] 누락된 학습 주제와 코드 보완
- [ ] 폴더별 간단한 README 또는 실행 방법 추가
- [ ] 실행되지 않는 실습 코드와 완료 예제를 구분
- [ ] DB 접속 정보·API 키 등 민감한 설정을 환경 변수로 분리
- [ ] 가상환경(`Lib/`, `Scripts/` 등), 캐시, 업로드 파일의 버전 관리 점검
- [ ] 학습 내용을 개념 → 코드 예제 → 결과 → 회고 순으로 정리

> ⚠️ 과거 실습 코드에는 로컬 DB 접속 정보가 직접 작성된 예제가 있습니다. 저장소를 공개 운영한다면 비밀번호·API 키가 실제로 사용 중인지 확인하고, 노출된 자격 증명은 교체한 뒤 환경 변수로 분리하는 것이 좋습니다.

---

### 🎯 학습 목표

**단순히 코드를 따라 치는 데서 끝나지 않고, 코드가 왜 이렇게 동작하는지 이해하는 개발자가 되는 것.**

작은 웹 화면과 문법 실습을 시작으로 데이터베이스를 활용한 백엔드 개발, 팀 협업, 데이터 처리와 AI 검색 기술까지 학습 범위를 확장한 과정을 이곳에 기록하고 있습니다.

*이 문서는 2026년 10월 28일 기준 저장소의 폴더 구조와 대표 코드를 바탕으로 정리했습니다.*
