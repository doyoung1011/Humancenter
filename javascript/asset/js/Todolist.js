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
  const todoInput = document.querySelector('#todoInput')

  addBtn.addEventListener('click', function (event) {
    const todolist_area = document.querySelector('.todolist_area')
    const todo = todoInput.value //이거를 위에서 찾기

    const div = document.createElement('div')

    todoInput.value = '' //초기화
    div.innerHTML = `
     할일 목록: ${todo}
     체크 리스트 <input type="checkbox" class='listChk'>
     개별 삭제<input type="button" class="remove"> 
     
     
  
  `
    todolist_area.prepend(div)

  //  
    const remove = document.querySelector('.remove')
    remove.addEventListener('click',function(event){
      div.remove()
      // this.parentNode.remove()
      // 이것도 가능!
      
    })

    //  할일 목록 추가 함수
  })

  const clearBtn = document.querySelector('#clearBtn')
  // 전체 취소하는 버튼

  clearBtn.addEventListener('click', function (event) {
    const todolist_area = document.querySelector('.todolist_area')
    todolist_area.innerHTML = ''

  })

  const allCheckBtn = document.querySelector('#allCheckBtn')
  allCheckBtn.addEventListener('click', function (event) {
    const listChk = document.querySelectorAll('.listChk')
    // 생성된 체크박스를 모두 반환
    console.log(listChk)
    // 체크박스가 체크되어있는지 확인하면됨
    for (let i = 0; i < listChk.length; i++) {
      listChk[i].checked = allCheckBtn.checked
    }
   
    // 이 버튼을 누르면 전체 선택
  })
  // 개별 삭제 버튼
  // const remvoe = document.querySelector('.remvoe')
  // remvoe.addEventListener('click', function (event) {
  //   if (event.target == checked) {

  //   }
  // })



}


/*
+ 5-1 : 추가버튼 누르면 체크박스와 할일이 하단에 추가된다
    + 5-2 : 개별 삭제 버튼이 있고, 클릭 시 그 줄이 지워진다 (dom.remove())
    + 5-3 : 전체 선택 checkbox가 있고
            전체 선택 체크 시 : 모든 checkbox 체크
            해제 시 : 모든 checkbox 체크 해제
    + 5-4 : 전체 선택 후 하나라도 개별 해제가 되면 전체 선택도 해제
            개별로 모두 체크한 경우 전체 선택도 체크된다
            이거 수행해야함
    + 5-5 : 선택 삭제 버튼 클릭 시 선택된 내용만 삭제

    엔터를 입력받아서 하는건 되긴하는데 정신없음

     전체 선택<input type="checkbox" id="allCheckBtn" />
     todolist_area.innerHTML = ''를 하게 되면 전체 삭제가됨

*/