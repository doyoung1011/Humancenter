# Humancenter
휴먼교육센터 학습기록

집에서 작성을 할경우 css파일 나누기 진행할 예정

간단하게 웹페이지를 카피해보기

지금까지 배운내용 적용시키기

호버링,flex사용해도 괜찮고 지금까지 배운 모든것을 적용시키기



<!-- 유튜브를 야매로 따라해보기 -->


2026-07-06 월요일 로그
유튜브 만들려면 검색창, 로고, 오른쪽에 추가영상

밑에 댓글창인데 이거는 만들수가 없으므로 패스

이정도하고 모바일대응 가능한걸 우선적으로 생각하기,

flex를 이용해서 가로 정렬할거고 inline-block사용

다양한 기술을 응용해서 사용해볼예정

searchbox 226*24로 커버(실제 유튜브 검색창 사이즈랑 동일)
추가 기술: 오른쪽에 영상들이 있는데 iframe으로 크기 조절해서 얼추 맞춰보기

그거랑 검색창을 센터로 좀 더 밀고 댓글창을 야매로 어케 구현해야할지 고민을 해봅시다



---------------------------------------------

잘못 설계한 코드를 기반으로 재 구조화 예정
 <!-- 최상단 감싸는 용도 -->
    <div class="wrapper">


        <div class="main">
            <div class="left_area">
                <a> <img src="https://upload.wikimedia.org/wikipedia/commons/d/dd/YouTube_Premium_logo.svg"
                        alt="유튜브프리미엄로고">
                </a>
                <div class="searchbox">
                    <input type="text" placeholder="검색">
                </div>
            </div>
            <!-- 여기에 왼쪽에 패딩을 주던 마진을 주함 약간 띄워야함 -->


            <div class="media">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/paJ8svJ1IoE?si=7E35vS3Z_XeLCEnS"
                    title="YouTube video player" frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
            </div>

            <div class="contents_container">
                구독/좋아요/댓글 공간
            </div>

            <div class="comment_area">
                댓글 공간
            </div>


            <!-- 화면 오른쪽에 나올 컨텐츠 -->
            <div class="right_area">
                <div class="<div class="searchbox">
                    <input type="text" placeholder="검색">
                </div>">
                    <div class="suggested_video_list">
                        추천영상 목록
                    </div>
                </div>
            </div>


        </div>


    </div>




    ----------구분선--------



    # Humancenter
휴먼교육센터 학습기록

집에서 작성을 할경우 css파일 나누기 진행할 예정

간단하게 웹페이지를 카피해보기

지금까지 배운내용 적용시키기

호버링,flex사용해도 괜찮고 지금까지 배운 모든것을 적용시키기



<!-- 유튜브를 야매로 따라해보기 -->


2026-07-06 월요일 로그
유튜브 만들려면 검색창, 로고, 오른쪽에 추가영상

밑에 댓글창인데 이거는 만들수가 없으므로 패스

이정도하고 모바일대응 가능한걸 우선적으로 생각하기,

flex를 이용해서 가로 정렬할거고 inline-block사용

다양한 기술을 응용해서 사용해볼예정

searchbox 226*24로 커버(실제 유튜브 검색창 사이즈랑 동일)
추가 기술: 오른쪽에 영상들이 있는데 iframe으로 크기 조절해서 얼추 맞춰보기

그거랑 검색창을 센터로 좀 더 밀고 댓글창을 야매로 어케 구현해야할지 고민을 해봅시다



---------------------------------------------

잘못 설계한 코드를 기반으로 재 구조화 예정
 <!-- 최상단 감싸는 용도 -->
    <div class="wrapper">


        <div class="main">
            <div class="left_area">
                <a> <img src="https://upload.wikimedia.org/wikipedia/commons/d/dd/YouTube_Premium_logo.svg"
                        alt="유튜브프리미엄로고">
                </a>
                <div class="searchbox">
                    <input type="text" placeholder="검색">
                </div>
            </div>
            <!-- 여기에 왼쪽에 패딩을 주던 마진을 주함 약간 띄워야함 -->


            <div class="media">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/paJ8svJ1IoE?si=7E35vS3Z_XeLCEnS"
                    title="YouTube video player" frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
            </div>

            <div class="contents_container">
                구독/좋아요/댓글 공간
            </div>

            <div class="comment_area">
                댓글 공간
            </div>


            <!-- 화면 오른쪽에 나올 컨텐츠 -->
            <div class="right_area">
                <div class="<div class="searchbox">
                    <input type="text" placeholder="검색">
                </div>">
                    <div class="suggested_video_list">
                        추천영상 목록
                    </div>
                </div>
            </div>


        </div>


    </div>
