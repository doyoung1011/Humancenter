console.log('hello js')

const btn1 = document.querySelector('#btn')

console.log(1, 'btn1', btn1)
console.log(window)

// 페이지 로딩 이벤트가 발생하면
// window.onload=function(){
//     const btn1=document.querySelector('#btn')

// console.log(2,'btn1', btn1)
// }

function init() {
    const btn1 = document.querySelector('#btn')
    console.log(2, 'btn1', btn1)

    // const game = document.querySelector('#game')
    // console.log(game.style.left)
}

// window.onload = init
window.addEventListener('load', init)
// 페이지 로딩이 끝나면 이벤트 작동함
function bind() {
    const btn1 = document.querySelector('#btn')

    btn1.onclick = function () {
        console.log('btn1 클릭')
    }
    btn1.onclick = function () {
        console.log('btn1 click')
    }
    const btn2 = document.querySelector('#btn2')
    console.log('btn2 click')
    btn2.addEventListener('click', function () {
        console.log('btn2 클릭')

    })
    btn2.addEventListener('click', function () {
        console.log('btn2 click')

    })

    const btn4 = document.querySelector('#btn4')
    btn4.addEventListener('click', btn4click)
    // removeEventListener
    // 이벤트 제거, 단 익명함수는 제거못함
    btn4.removeEventListener('click', btn4click)
}
// function btn3click(){
//     console.log('btn3 click')
// }
// function btn4click(){
//     console.log('btn4 click')
// }


console.log('-------------------구분용-------------------')


const login = document.querySelector('#login')


login.addEventListener('click', function () {
    const id = document.querySelector('#id')
    const pw = document.querySelector('#pw')
    const warning = document.querySelector('.warning')
    console.log(id.value)
    console.log(pw.value)

    // id를 적었는지 판단
  if (id.value.trim() == '') {

    console.log('아이디는 필수입니다')//이건 그냥 확인용
    warning.innerText = '아이디는 필수 입니다'// 이너텍스트로 내용 넣기

    log('아이디는 필수입니다')

    // <div class="log">글씨 출력</div>

}
else if (pw.value.trim() == '') {
    console.log('아이디는 필수입니다')
    warning.innerText = '비밀번호는 필수 입니다'


    log('비밀번호는 필수입니다')
}
document.querySelector('#id').addEventListener('keyup', function (event) {
    // log('keyup 발생')
    // console.log(event)// 콘솔로 찍어서 뭐나오나 확인
    // log('key' + event.key)
    // log('keyCode:' + event.keyCode)

    // log('shiftKey:' + event.shiftKey)
    // log('ctrlKey:' + event.ctrlKey)
    // log('alterKey:' + event.alterKey)

    if(event.keyCode==13){
        //엔터
        log('엔터 뽱!')
        const pw = document.querySelector('#pw')
        pw.focus(   )
    }

    if(event.ctrlKey && event.keyCode ==67){// 복사방지 코드
        alert('ctr1+c 금지!')
    }
}
)
document.querySelector('pw').addEventListener('keyup',function(event){
    if(event.keyCode==13){
        //엔터일경우
        const login=document.querySelector('#login')
        login.click()
    }
})


}

)





function btn3click() {
    console.log('btn3 click')
}
function btn4click() {
    console.log('btn4 click')
}

//콘솔창 대체용으로 사용할것
function log(message) {
    const div = document.createElement('div')
    div.classList.add('log')
    div.innerHTML = message

    const view = document.querySelector('#view')
    view.prepend(div)
}
