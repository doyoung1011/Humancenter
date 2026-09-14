// 로그인 팝업 로직임
window.onload = () => {
    document.querySelector('.popup .close').addEventListener(
        'click', function (event) {

            console.log(event.target.parentElement.parentElement)

            event.target.parentElement.parentElement.classList.add('hide')
            if (event.target.parentElement.querySelector('.chk').checked) {
                document.cookie = `loginPopup=True;  max-age=${60 * 60 *24}; path=/`
            }
            
        }
    )
    value=getCookieValue('loginPopup')

    if(value!=null){
        document.querySelector('.popup').classList.add('hide')
    }
   
} 

function getCookieValue(key){
    cookies=document.cookie.split('; ')
    
    for(cookie of cookies)
        
        names=cookie.split('=')[0]
        value=cookie.split('=')[1]

        if(names==key){
            return value
        }
        return null
}