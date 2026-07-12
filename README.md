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


-----------------------------------------------------------------------------------
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- <link rel="stylesheet" href="../css/login.css"> -->
    <style>
        * {
            border: 1px solid red;
        }
        body {
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .wrapper {
            /* display: inline-block; */
            width: 500px;
            padding: 20px
        }

        .logo {
            text-align: left;
            font-size: 20px;
            font-weight: bold;
            color: green;
            box-sizing: border-box;
            border-color: black;
        }
        .index{
            width: 100%;
            margin: 0 auto;
        }
    </style>
</head>
</head>

<body>

    <div class="wrapper">
        <div class="index">
            <div class="logo">네이버</div>
            <form action="http://127.0.0.1:5501/html/main.html" method="get">
                <div class="input_id">
                    <input type="text" placeholder="이메일을 입력">
                </div>
                <div class="input_pw">
                    <input type="password" placeholder="비밀번호를 입력">
                    <button type="submit">login</button>
            </form>
        </div>
    </div>

</body>

</html>
로그인 페이지 야매구성


----------------------------------------------------------------------------------------------------------------------

문제1
  10개의 각 변수에 1~10까지 담기
  변수 선언 10개의 변수를 담을 방을 구성
결론:[1,2,3,4,5,6,7,8,9,10]
  
*/
    const arrz = [];

    for (let i = 1; i < 11; i++) {
      arrz.push(i);
    }
    console.log(arrz);

    /*
문제2
  [3,4,7,5,1,6]
  문제 2-1
  홀수의 개수 구하기-> 홀수는 나누었을때 나머지가 1 이고 그걸 세면됨
 
  그러면 num의 요소%2!=0글이면 됨

  문제 2-2
  4보다 큰 수의 개수 구하기
  
*/
    // //  문제 2-1부터
    // let count = 0;
    // const num = [3, 4, 7, 5, 1, 6];
    // for (let i = 0; i < num.length; i++) {
    //   if (num[i] % 2 != 0) {
    //   count++
    // 여기서 헷갈린 부분 count++은 이미 변수에 담는 개념임 count+=count이기 때문임
    // count는 홀수가 나온걸 세는 변수임

    //   }
    // }
    // console.log(`홀수의 개수 ${count}개입니다`); //이러면 끝

    let count = 0;
    const num = [3, 4, 7, 5, 1, 6];
    for (let i = 0; i < num.length; i++) {
      if (num[i] > 4) {
        count++;
      }
    }
    console.log(`4보다 큰수의 개수는 ${count}개입니다`);

    //완주를 한사람은 음번밖에 없음 그렇다면 3번만 솎아내면됨
    //나는 3번이 실패한 걸 알지만, 컴퓨터는 그걸 몰라서 그 리스트에 있는지 확인해야함
    // let flag=0 //마라톤을 실패한 사람
    // 오타 주의


    let marathon = [1, 2, 3, 4, 5]; //마라톤 참가 리스트
    let succes = [2, 4, 5, 1]; //성공한 사람 담음
    let fail = 0 //  이따가 실패한 사람을 담을 공간

    for (i = 0; i < marathon.length; i++) {
      let flag = false  //아직 실패자를 못찾았다는 상태 코드임
      for (j = 0; j < succes.length; j++) {
        if (succes[j] == marathon[i]) { // 만약 성공자와 전체리스트가 같다면이라는 조건
          flag = true
          break // 반복문 탈출
        }

      }

      if (flag == false) {
        fail = marathon[i]
        break
      }
    } console.log(`탈락하신분은: ${fail}`)

    // 문제3-1
    참가목록: ['나미', '우솝', '조로', '루피', '상디']
    완주목록: ['우솝', '나미', '상디', '조로']

    let list = ['나미', '우솝', '조로', '루피', '상디']
    let clear = ['우솝', '나미', '상디', '조로']
    let fail_list = 0

    for (i = 0; i < list.length; i++) {
      let flag = false  //아직 실패자를 못찾았다는 상태 코드임
      for (j = 0; j < clear.length; j++) {
        if (clear[j] == list[i]) { // 만약 성공자와 전체리스트가 같다면이라는 조건
          flag = true
          break // 반복문 탈출
        }

      }

      if (flag == false) {
        fail_list = list[i]
        break
      }
    } console.log(`탈락하신분은: ${fail_list}`)


    //문제 4-1

    let seat_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] // 예약 번호
    let reservation = [] // 예약 좌석
     menu = prompt(`1: 예약 2:모든 좌석 현황 3:잔여 좌석 4: 종료`)

    for (let i = 0; i < seat_num.length; i++) {
      let flag = false

      for (j = 0; j < reservation.length; j++)
        if (seat_num[i] == reservation[j]) {
          reservation.push(seat_num[i])
        }
    } console.log(reservation[j])



