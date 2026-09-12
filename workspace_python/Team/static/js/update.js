const init = () => {
    bind()
}

window.onload = init

const bind = () => {
    const menuList = document.querySelector('#menu-list')
    const menuAdd = document.querySelector('#menu-add')

    menuAdd.addEventListener('click', function () {
        const menuRow = document.createElement('div')
        menuRow.className = 'menu-row'
        menuRow.innerHTML = `
            <input
                type="text"
                name="menu_name"
                class="menu-name"
                placeholder="메뉴명을 입력해 주세요."
                maxlength="20"
            >

            <div class="price-input">
                <input
                    type="number"
                    name="price"
                    class="menu-price"
                    placeholder="0"
                    min="0"
                    step="100"
                >
                <span>원</span>
            </div>

            <button type="button" class="menu-delete">삭제</button>
        `
        menuList.append(menuRow)
    })
 
    menuList.addEventListener('click', function (event) {
        if (event.target.classList.contains('menu-delete')) {
            event.target.parentElement.remove()
        }
    })
}