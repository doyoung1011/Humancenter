// 로그인 팝업 로직임
window.addEventListener('load', () => {
    // document.querySelector('.popup .close').addEventListener(
    //     'click', function (event) {

    //         console.log(event.target.parentElement.parentElement)

    //         event.target.parentElement.parentElement.classList.add('hide')

    //         console.log(event.target.parentElement.querySelector('.chk'))
    //         console.log(event.target.parentElement.querySelector('.chk').checked)

    //         if (event.target.parentElement.querySelector('.chk').checked) {
    //             document.cookie = `loginPopup=True; max-age=${60 * 60 *24}; path=/`
    //         }
            
    //     }
    // ) 
    // value=getCookieValue('loginPopup')
    // console.log('value : ', value)

    // // if(value!=null){
    // //     document.querySelector('.popup').classList.add('hide')
    // // }

    const popup = document.querySelector('.popup')
    const chk = document.querySelector('.chk')
    const close = document.querySelector('.close')    

    close.addEventListener('click',function(){
        popup.classList.add('hide')
    // 체크되어있으면 하루동안 팝업을 숨기는 쿠키를
        if(chk.checked == true) {
            document.cookie = `popup=close; max-age=${60 * 60 *24}; path=/`
        }
    })

    const cookies = document.cookie.split('; ')
    console.log(cookies)

    for(i=0; i<cookies.length; i++) {
        if(cookies[i]!='popup=close'){
            popup.classList.remove('hide')
        } else {
            popup.classList.add('hide')
            break
        }
    }


        // for(cookie of cookies){
        //     console.log(cookie)

        //     cookie.split('=')

        //     let name = ''
        //     let value = ''

        //     if(cookie.split('=')[1] == 'close'){
        //         console.log('쿠키클로즈에요', cookie)

        //         name = cookie.split('=')[0]
        //         value = cookie.split('=')[1]

        //         console.log('name : ', name)
        //         console.log('value : ', value)
        //     }
            
        // }
        
    // testCookies = document.cookie.split('; ')

    // for(tCookie of testCookies) {
    //     if(tCookie[i] == 'loginPopup=True'){
    //         document.querySelector('.popup').classList.add('hide')
    //     } else {
    //         document.querySelector('.popup').classList.remove('hide')
    //     }
    // }
   
})

function getCookieValue(key){
    cookies=document.cookie.split('; ')
    console.log('cookies : ', cookies)

    for(cookie of cookies){
        
        console.log('cookies : ', cookie)

        names=cookie.split('=')[0]
        value=cookie.split('=')[1]

        console.log('names : ', names)
        console.log('value : ', value)

        if(names==key){
            return value
        }
        return null
        }
}