window.addEventListener('load', bind)


// 2번
function bind() {


    const btn1 = document.querySelector('#btn1')
    btn1.addEventListener('click', function () {
        debugger
        // 성jax 객체생성
        const xhr = new XMLHttpRequest()
        //  보낼 준비
        // 방식
        xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')
        // xhr.open('GET','19_json.html')

        // 보내기 
        xhr.send()

        xhr.onload = function () {
            console.log('다녀왔어')
            console.log(xhr.responseText)
            // 깜짝 퀴즈
            // 두번째 사람의 이름을 출력
            // 
            const member = JSON.parse(xhr.responseText)
            console.log(member[1].name)//두번재 사람의 이름

            console.log(member[2].address.geo.lat)


        }



    })
    // const btn2 = document.querySelector('#btn2')
    // btn2.addEventListener('#btn2')

    //잠시 버튼 3번 비활성화

    // const btn3 = document.querySelector('#btn3')
    // btn3.addEventListener('click', function () {

    //     const now = new Date()// 실시간 날짜를 잡아옴
    //     const today = now.toISOString('T')[0].split('T')[0].replace(/-/g, '')
    //     let hour = now.getHours() - 1
    //     if (hour < 10) {
    //         hour = '0' + hour + '00'
    //     } else {
    //         hour = hour + '00'
    //     }
    //     const key = '2cdc27a5fd6ffdd825a2ed0944039c5626edbd8f65a08d40cd0d7b5fbfbef205'

    //     let url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
    //     url += '?'
    //     url += 'serviceKey=' + key
    //     url += '&numOfRows=1000'
    //     url += '&pageNo=1'
    //     url += '&dataType=JSON'
    //     url += '&base_date=20260722'
    //     url += '&base_time=1500'
    //     url += '&nx=63'
    //     url += '&ny=110'

    //     const xhr = new XMLHttpRequest()// ajax 객체 생성
    //     xhr.open('get', url) //보낼 준비
    //     xhr.send()// 보내기 

    //     xhr.onload = function () {



    //         const data = JSON.parse(xhr.responseText) //텍스트 파일로 오니까 json파일로 바꿔줌
    //         console.log(data)

    //         console.log(data.response.body.items.item[0].category)
    //         console.log(data.response.body.items.item[0].fcstValue)
    //         console.log(data.response.body.items.item[0].fcstTime)



    //         // 데이터를 까보면 category가 TH1(기온),RN1(강수량), REH(습도)임

    //         let item = data.response.body.items.item
    //         // item.filter(function (data) {
    //         //     // console.log(data)
    //         // })

    //         let filterd = item.filter(function (data) {
    //             if (data.category == 'TH1'
    //                 || data.category == 'RN1'
    //                 || data.category == 'REH'
    //             ) {
    //                 return true
    //             }
    //         })
    //         console.log(filterd)

    //         //  문제 1번시작
    //         // fcstTime이 예측 시간, fcstValue를 그냥 출력하면 될거같음
    //         //  테이블에다가 넣기해서

    //         const q1 = document.querySelector('#q1')
    //         for (let i = 0; i < filterd.length; i++) {
    //             const tr = document.createElement('tr')//tr이라는 변수에 넣음
    //             tr.innerHTML = `
    //         <td>${filterd[i].category}</td>
    //         <td>${filterd[i].fcstTime}</td>
    //         <td>${filterd[i].fcstValue}</td>
    //      `
    //             q1.append(tr)
    //         }
    //         // 자바스크립트로 html 테이블에 내용을 추가함
    //         //  여기까지 문제 1번임



    //         // 문제 2번
    //         // 시간, 온도,습도,강수량 테이블이 나오게

    //         /*
    //         시간을 key값으로 가져가면 더 편할거같음

    //         */


    //         // let j = {
    //         //     '1000': {
    //         //         'TH1': 20,
    //         //         'REH': 80,
    //         //         'RN1': '2.0 mm'
    //         //     }
    //         // }

    //         // j = {} //j는 빈 json
    //         // for (let i = 0; i < filterd.length; i++) {
    //         //     if (j[filterd[i].fcstTime] == undefined) {
    //         //         j[filterd[i].fcstTime] = {}// 만약 없으면 json 초기화 진행
    //         //     }
    //         //     j[filterd[i].fcstTime][filterd[i].category] = filterd[i].fcstValue
    //         // }

    //     }



    // })
    // 테이블로 표시
    // 문제 1번
    // 예측 카테고리, 예측시간, 값
    // 문제 2번



    // 시간, 온도,습도,강수량 테이블이 나오게


    const btn4 = document.querySelector('#btn4')
    btn4.addEventListener('click', function () {
        const xhr = new XMLHttpRequest()// ajax 객체 생성
        xhr.open('get', 'https://jsonplaceholder.typicode.com/users') //보낼 준비
        xhr.send()// 보내기 
        // 아작스 준비까지는 구현
        // innerHTML로 테이블 구조 그대로 갖다 붙힐 예정


        xhr.onload = function () {
            const memberData = JSON.parse(xhr.responseText)
            console.log(memberData)// 오는 파일에 텍스트라서 변환
            const q4 = document.querySelector('#q4')

            console.log(q4)
            // tbody안에 잘들어갔나 확인
            q4.innerHTML=''
            for (let i = 0; i < memberData.length; i++) {
                const trs = document.createElement('tr')
                // tr에다가 쑤셔넣기
                // 근데 쑤셔넣기 전에 필터로 한번 걸려줘야함
                // id,name,zipcode,회사이름
                // let item = data.response.body.items.item
                trs.innerHTML = ` 
                     <td>${memberData[i].id}</td>
                     <td>${memberData[i].name}</td>
                       <td>${memberData[i].address.zipcode}</td>
                     <td>${memberData[i].company.name}</td>
                        `
                q4.append(trs)
            }




        }
        // name->이름으로, zipcode를 주소로 회사이름을 ghl













    })
    const btn5 = document.querySelector('#btn5')
    btn5.addEventListener('click', function () {
        const url = 'https://jsonplaceholder.typicode.com/users'

        fetch(url, {
            method: 'GET'
        }).then(function (response) {
            console.log(response)
            return response.json()

        }).then(function (data) {
            console.log(data)
        }).catch(function (e) {
            console.error(e)
        })

    })




}