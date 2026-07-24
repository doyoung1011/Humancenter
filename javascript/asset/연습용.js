window.onload = function () {
    bind()
}


function bind() {
    // event.stopPropagation()
    // 부모로 전달되는 이벤트 방지
    // event.target 이벤트가 발생한 타겟

    //  step 1.일단 클릭을 했을떄. 굵은 글씨를 만들기
    // btn이라는 하나의 클래스를 줘서 이벤트 타겟으로 잡아옴
    const btn = document.querySelectorAll('.btn')
    // 그러면 클릭할떄마다 작동하는 함수를 제작
    // 쿼리 셀렉터 유사배열이라,요소[i] 적용 이렇게 제작

    for (let i = 0; i < btn.length; i++) {
        btn[i].addEventListener('click', function (event) {
            // 여기에 초기화 코드를 넣으믄 되지 않을카

            for (let j = 0; j < btn.length; j++) {

                btn[j].style.fontWeight = 'normal'
                btn[j].style.textDecoration = 'none'

            }
            console.log(event.target)
            btn[i].style.fontWeight = 'bold'
            btn[i].style.textDecoration = 'underline'

        })


    }





    // for(let i)



}





