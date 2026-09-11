const init = () => {
    bind()
}

window.onload = init

const bind = () => {
    const checkButton = document.querySelector('.check-button')
    const idCheck = document.querySelector('#id-check')
    const numCheck = document.querySelector('#num-check')
    const password = document.querySelector('#password')
    const passwordConfirm = document.querySelector('#password-confirm')
    const passwordWarning = document.querySelector('#password-warning')

    idCheck.addEventListener('click', function(){
        const id = document.querySelector('#login-id')
        console.log(id.value)

        // id 중복 확인인데 아직 미완성
        // if(id.value.trim() == ''){
        //     console.log('아이디는 필수입니다')
        //     warning.innerText = '아이디는 필수입니다'
        // } else if(id.value.trim() == ''){
        //     console.log('중복된 아이디입니다')
        //     warning.innerText = '중복된 아이디입니다'
        // }

    })

    numCheck.addEventListener('click', function(){
        const phone = document.querySelector('#phone')
        console.log(phone.value)
    })

    // 비밀번호 중복
    passwordConfirm.addEventListener('input', function(){
        if(password.value != passwordConfirm.value && password.value.length >= 1){
            console.log('비밀번호가 일치하지 않습니다.')
            passwordWarning.innerText = '비밀번호가 일치하지 않습니다.'
        } else {
            passwordWarning.innerText = ''
        }
    })
}