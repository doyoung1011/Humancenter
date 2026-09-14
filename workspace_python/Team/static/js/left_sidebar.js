window.addEventListener('load', () => {
    sidebarToggle = document.querySelector('.sidebar-toggle')
    sidebarContent = document.querySelector('.sidebar-content')
    sidebarToggle.addEventListener('click', function() {
        if (sidebarContent.style.display == 'none') {
            sidebarContent.style.display = ''
        } else {
            sidebarContent.style.display = 'none'
        }
    })
})