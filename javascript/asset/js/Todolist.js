window.onload = function () {
  bind()
}
// 엔터를 입력했을때도 가능하도록

function bind() {
  // <input type="text" id="TodoInput"> 
  //  사용자가 입력한 값을 가져와야함
  // value로 가져옴
  // 자바스크립트로 체크버튼 가져옴
  // const addBtn = document.querySelector('#addBtn')
  // 이거 다시 살려내야겄다.
  // 사용자가 입력한 값을 저장할 변수 제작
  const addBtn = document.querySelector('#addBtn')
  const todoInput=document.querySelector('#todoInput')

  addBtn.addEventListener('click', function (event) {

    const todolist_area = document.querySelector('.todolist_area')
    const todo = todoInput.value //이거를 위에서 찾기

    const div = document.createElement('div')

    //innerHTML로 할일목록을 떄려넣을 예정임

    div.innerHTML = `
     ${todo}
  
  `
    todolist_area.prepend(div)



    //  할일 목록 추가 함수








  })

}


/*
+ 5-1 : 추가버튼 누르면 체크박스와 할일이 하단에 추가된다
    + 5-2 : 개별 삭제 버튼이 있고, 클릭 시 그 줄이 지워진다 (dom.remove())
    + 5-3 : 전체 선택 checkbox가 있고
            전체 선택 체크 시 : 모든 checkbox 체크
            해제 시 : 모든 checkbox 체크 해제
    + 5-4 : 전체 선택 후 하나라도 개별 해제가 되면 전체 선택도 해제
            개별로 모두 체크한 경우 전체 선택도 체크된다
    + 5-5 : 선택 삭제 버튼 클릭 시 선택된 내용만 삭제

    엔터를 입력받아서 하는건 되긴하는데 너무 없음....

*/