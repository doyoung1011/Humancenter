window.addEventListener('load', bind)


// 2번
function bind() {


    const btn1 = document.querySelector('#btn1')
    btn1.addEventListener('click', function () {
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


    const btn3 = document.querySelector('#btn3')
    btn3.addEventListener('click', function () {
        const key = '2cdc27a5fd6ffdd825a2ed0944039c5626edbd8f65a08d40cd0d7b5fbfbef205'

        let url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
        url += '?'
        url += 'serviceKey=' + key
        url += '&numOfRows=1000'
        url += '&pageNo=1'
        url += '&dataType=JSON'
        url += '&base_date=20260722'
        url += '&base_time=1500'
        url += '&nx=63'
        url += '&ny=110'

        const xhr = new XMLHttpRequest()// ajax 객체 생성
        xhr.open('get', url) //보낼 준비
        xhr.send()// 보내기 

        xhr.onload = function () {
            const data = JSON.parse(xhr.responseText) //텍스트 파일로 오니까 json파일로 바꿔줌
            console.log(data)

            console.log(data.response.body.items.item[0].category) 
            console.log(data.response.body.items.item[0].fcstValue)
            console.log(data.response.body.items.item[0].fcstTime)



            // 데이터를 까보면 category가 TH1(기온),RN1(강수량), REH(습도)임

            let item = data.response.body.items.item
            // item.filter(function (data) {
            //     // console.log(data)
            // })

            let filterd=item.filter(function(data){
                if(data.category=='TH1'
                    || data.category=='RN1'
                    || data.category=='REH'
                ){
                    return true
                }
            })
             console.log(filterd)

            //  문제 1번시작
            // fcstTime이 예측 시간, fcstValue를 그냥 출력하면 될거같음
            //  테이블에다가 넣기해서
        
            const result=document.querySelector('#result')// id 보고 찾아감
            result.innerHTML='' // 내용을 추가할 것 




        }

    })
    // 테이블로 표시
    // 문제 1번
    // 예측 카테고리, 예측시간, 값
    // 문제 2번
    // 시간, 온도,습도,강수량 테이블이 나오게




}