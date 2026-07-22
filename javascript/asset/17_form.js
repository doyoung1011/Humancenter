function log(message) {
    const div = document.createElement('div')
    div.classList.add('log')
    div.innerHTML = message

    const view = document.querySelector('#view')
    view.prepend(div)
}

window.addEventListener('load', function () {

    const query = document.querySelector('#query')
    query.addEventListener('focus', function () {
        query.style.background = 'yellow'
    })

    query.addEventListener('blur', function () {
        query.style.background = ''
    })
    // input은 값이 변경될 떄 잡아주는 이벤트
    query.addEventListener('input', function () {
        log('1')
        log(query.value)

        const r = parseInt(Math.random() * 256)
        const g = parseInt(Math.random() * 256)
        const b = parseInt(Math.random() * 256)
        const a = Math.random()

        query.style.backgroundColor = `rgba(${r},${g},${b},${a})`

    })
    const form = document.querySelector('#form')
    form.addEventListener('submit', function (event) {

        event.preventDefault()//태그의 기본(고유)기능을 막아준다.

        if (query.value.trim().length < 2) {
            alert('검색어는 두 글자 이상입니다')
        } else {
            form.submit()
        }

    })
    const parent = document.querySelector('#parent')
    parent.addEventListener('click', function (event) {
        log('부모클릭')
        // target: 실제 이벤트가 발생한 DOM
        console.log('event.target', event.target)
        // currentTarget: 이벤트가 적용되어 있는 DOM
        console.log('event.currenttarget', event.currentTarget)

        // this
        // addEventListener 안에서는 event.currentTarget
        // 대부분의 경우 window를 가지고 있다
        // 그래서 현재 this에 어떤 값이 있는지 알고 있을 떄만 사용
        // arrow 함수의 경우 this==window
        console.log('this', this)
        console.log(this === event.currentTarget)
    })

    const child1 = document.querySelector('#child1')
    child1.addEventListener('click', function () {
        // 전달 방지
        // 부모로 전달되는 이벤트 중지
        event.stopPropagation()
        log('자식 1클릭')
    })

    const child2 = document.querySelector('#child2')
    child2.addEventListener('click', function () {
        // 전달 방지
        // 부모로 전달되는 이벤트 중지
        event.stopPropagation()
        log('자식 2클릭')
    })
    // 1. click된 dom을 출력하시오
    // 2. 지금 클릭 요소에 클래스 chk가 있는지 출력
    // 3 만약 체크박스 일떄만 value를 출력하시오
    // 4.제목을 클릭했을 때 글씨 출력
    // 5.작성자를 클릭하면 속성 writer의 값이 나오도록
    // 6. table말고 tr에 위임하는 방법
    // 7. 체크를 하면 제목이 출력되도록..!
    const board = document.querySelector('#board')
    board.addEventListener('click', function (event) {
        event.stopPropagation() //부모로 전달되는 이벤트 중지
        console.log(event.target)
        // 클래스의 존재 여부 파악하기
        // 클래스 복습하기
        if (event.target.classList.contains('chk')) {
            log(event.target.value)
        }
        if (event.target.classList.contains('title')) {
            log(event.target.textContent)
        }

        if (event.target.hasAttribute('writer')) {
            log(event.target.getAttribute('writer'))
        }
        //    속성을 가져오는 방법

    })

    const trs = document.querySelectorAll('#board tr')
    for (let tr of trs) { //배열의 처음부터 끝까지
        tr.addEventListener('click', function (event) {
            event.stopPropagation() //부모로 전달되는 이벤트 중지
            console.log(event.target)
            // 클래스의 존재 여부 파악하기
            // 클래스 복습하기
            if (event.target.classList.contains('chk')) {
                log(event.target.value)
            }
            if (event.target.classList.contains('title')) {
                log(event.target.textContent)
            }

            if (event.target.hasAttribute('writer')) {
                log(event.target.getAttribute('writer'))
            }
            //    속성을 가져오는 방법

        })
        // tr중에서 체크박스만 골라내서 이벤트 넣기
        tr.querySelector('input.chk').addEventListener('click', function (event) {
            event.stopPropagation()

            //   console.log(this.parentNode)
            this.parentNode.parentNode.querySelector('.title').innerText
            // 여행을 떠내서 원하는 지점으로 안착하는 방법
            // 줄안에서
        })
    }
    //  const order=document.querySelector('#order_information')

    const order_name = document.querySelector('.order_name')
    // console.log(order_name.value); //값이 들어가는지 확인

    const order_address = document.querySelector('.order_address')

    const delivery_name = document.querySelector('.delivery_name')
    const delivery_address = document.querySelector('.delivery_address')

    // console.log(order_name.value)

    //  js로 값을 찾는과정

    // 밑에는 체크되었을때 덮어쓰는 코드
    const same = document.querySelector('#check').addEventListener('click', function (event) {



        if (event.target.checked) { // 체크박스가 체크되어있다면 
            delivery_name.value = order_name.value
            delivery_address.value = order_address.value //복사는 되지만 무조건적으로 복사가 됨
        } else {
            delivery_name.value = ""
            delivery_address.value = ""//복사는 되지만 무조건적으로 복사가 됨
        }
        console.log(event.target.checked)

        // checked는 true/false값을 반환함
        // 그렇기에 event.target== checked로 비교하는 것이 아니라
        // event.target.checked로 비교함 


    })

    // 2번 문제
    /*
    문제 2: 로그인창
    로그인 버튼 눌렀을 떄:구현 
    아이디/비밀번호 없으면 빨간 글씨 나옴: 조건 넣기
    빨간 글씨를 넣을려면 스타일을 넣으면 됨
    단, 아이디/비밀번호를 쓰고 로그인 누르면->else문에다가 떄려넣기
    빨간 글씨 지우기.
    */
    const id = document.querySelector('#id')
    const pw = document.querySelector('#pw')
    const warning = document.querySelector('.warning') // 등록해줌-> 색깔 바꾸는 코드

    const login = document.querySelector('#login').addEventListener('click', function (event) {
        // pw.value.trim() == ''// 비밀번호 입력안되었을때
        // id.value.trim()==''// 아이디 입력 X상황
        if (id.value.trim() == '') {
            warning.innerText = '아이디는 필수 입니다'// 이너텍스트로 내용 넣기
            warning.style.color = 'red'

        }
        else if (pw.value.trim() == '') {
            warning.innerText = '비밀번호는 필수 입니다'
            warning.style.color = 'red'

        }
        else {
            warning.innerText = ""
            console.log(warning.innerText)

        }

    })
    //3번 문제
    const pizza = document.querySelector('#pizza')
    const result = document.querySelector('#result')
    // const label = document.querySelector()
    //   
  


})



// console.log(this)

/*
    문제 1:주문과 배송
    주문 정보: input으로 이름과 주소
    주문정보와 배송정보가 같습니다
    배송 정보: input으로 이름과 주소

    *체크하면 주문 정보가 배송 정보로 복사됨
    *체크풀면  배송 정보 글씨 지우기

    문제 2: 로그인창
    로그인 버튼 눌렀을 떄
    아이디/비밀번호 없으면 빨간 글씨 나옴
    단, 아이디/비밀번호를 쓰고 로그인 누르면
    빨간 글씨 지우기.
    
    문제 3: 피자 주문
    1. 피자 종류 선택:selct
    -불고기 피자, 페페로니, 포테이토, 치즈, 파인애플, 고르곤졸라
    2. 사이즈 선택: radio
    -small(18000),midium(20000), large(22000)
    3. 도우 선택: radio
    -씬, 고구마, 치즈
    4. 토핑 : checkbox
    -감자(2000), 고구마(2000), 치즈(2500), 베이컨(3000), 옥수수(500)
    [확인] 버튼 존재
    +문제 3-1: 선택 내역 모두 출력하기.
    +문제 3-2: 선택 내역과 총액 출력

    문제 4: 메뉴 선택
    인기상품순, 낮은가격순, 높은가격순, 신상품순, 상품평 많은 수
    클릭한 것만 굵은 글씨로 유지

    문제 5: Todo list

    

*/

/*
문제 1번 부터 해결해보자
*/