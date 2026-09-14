const init = () => {
    bind()
}

window.onload = init

const bind = () => {
    // 수정 버튼 누르면 생기는일
    document.querySelector('.update-btn').addEventListener('click',function(){
        alert('내정보가 수정되었습니다!')

    })
}