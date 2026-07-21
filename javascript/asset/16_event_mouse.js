let _isDrag = false //드래그가 되기전 상태 
let _offsetX = 0
let _offsetY = 0


//콘솔창 대체용으로 사용할것
function log(message) {
    const div = document.createElement('div')
    div.classList.add('log')
    div.innerHTML = message

    const view = document.querySelector('#view')
    view.prepend(div)
}
window.onload = function () {
    bind()
}
function bind() {
    //이벤트 처리 묶어두는용

    const area = document.querySelector('#area')
    area.oncontextmenu = () => {
        alert("우클릭 금지!")
        return false
    }
    area.onselectstart = function () {
        return false
    }

    const area2 = document.querySelector('#area2')
    area2.addEventListener('copy', function (event) {
        event.preventDefault()
        const selection = window.getSelection().toString()
        console.log(selection)

        if (selection.length == 0) {
            return
        }
        const str = '[출처] www.naver.com'
        const result = selection + str
        event.clipboardData.setData('text/plain', result)


    })
    area2.addEventListener('mousedown', function () {
        log('mousedown')

    })
    area2.addEventListener('mouseup', function () {
        log('mouseup')

    })

    area2.addEventListener('click', function (evt) {
        log('click')

        /*
          offset: DOM 최상단 기준
          page: 스크롤에 관계없이 문서 최상단 기준
          
          client: 지금 보이는 브라우저 최상단 기준
          screen: 실제 모니터 최상단 ㄴ
        */
        log('offsetY: ' + evt.offsetY)
        log('pageY: ' + evt.pageY)
        log('clientY: ' + evt.clientY)
        log('screen: ' + evt.screenY)

    })
    area.addEventListener('mouseover', function (evt) {
        log('mouseover')
        area2.style.backgroundColor = 'yellow'
    })


    area.addEventListener('mouseout', function (evt) {
        log('mouseout')
        area2.style.backgroundColor = 'blue'
    })
    area.addEventListener('mousemove', function (evt) {//마우스 움질일때!
        log('mousemove')
        // log(`offsetX:${evt.offsetX}, offsetY:${evt.offsetY}`)
    })

    document.querySelector('body').addEventListener('mousemove', function (evt) {
        const game = document.querySelector('#game')
        game.style.top = evt.clientY + 'px'
        game.style.left = evt.clientX + 'px'

        // 마우스로 그림 움직이기

    })

    document.querySelector('#img').addEventListener('mousedown', function (evt) {
        _isDrag = true
        evt.offsetX
    })
    document.querySelector('#img').addEventListener('mouseup', function (evt) {
        _isDrag = false
    })
    document.querySelector('body').addEventListener('mousemove', function (evt) {
        const img = document.querySelector('#img')

        if (_isDrag) {
            img.style.top = (evt.clientY - _offsetY) + 'px'
            img.style.left = (evt.clientX - _offsetX)+ 'px'
        }// 드래그 기능


       window.addEventListener('resize',function(){
        const w=window.innerHeight
        const h=window.innerWidth

        log(`w:${w},h:${h}`)
       })
       
  

    })



}