window.onload = function () {
  bind()
}
function bind() {
  const order = document
    .querySelector('#order')
    .addEventListener('click', function (event) {
      const result = document.querySelector('#result')

      // 이따 출력용이라서 뺴둠
      const size = document.querySelector('input[name="size"]:checked')
      const _size = parseInt(size.getAttribute('price'))
      // 가격 계산을 위한 코드
      //    이거는 체크박스라서 그런거임

      const pizza = document.querySelector('#pizza')
      // 이거는 피자 종류 찾아가기
      const dough = document.querySelector('input[name="dough"]:checked')


      const topping = document.querySelectorAll('input[name="topping"]:checked')

      //제대로 생각도 못해밨는데 전체에서 요소를 꺼내서 찾아야함
      // 백틱으로 전부 다쓸꺼임
      // result.innerText=`선택한 피자는 ${pizza.value}피자입니다`
      // log(size .value)
      let toppingText = ''
      let topping_price = 0
      for (let i = 0; i < topping.length; i++) {
        // for문안에서 토핑 가격 합산 코드도 합산
        toppingText += topping[i].getAttribute('value') + ' '
        topping_price += parseInt(topping[i].getAttribute('price'))
        //NodeList라서 요소 i를 사용함
      }
      //   버튼을 눌렀을때 선택한 토핑을 출력하는 방법.
      // 여기에 가격계산코드

      // 가격은 사이즈+토핑가격+도우가격임
      const total_price = _size + topping_price

      result.innerText = ` 피자: ${pizza.value} 사이즈: ${size.value} 토핑: ${toppingText}
    도우: ${dough.value} 총 주문금액은: ${total_price}원 입니다`



    })
}

//parseInt로 묶어서 value를 잡은 다음에 계산 수행.

/*

html 코드에서 price 항목 추가후, 전체적으로 추가

size 항목에서 price 가져오는법  cosnt sieze= checkd.getAttribute('price')// 선택된것 중에 항목이
price인거 나머지도 이렇게 가져오면 될거 같고, 여기서 pareInt로 감싸서 문자형-> 숫자로 변환 수행



<label
      ><input
        type="radio"
        class="size"
        value="Small"
        price="18000"
        name="size"
      />Small</label
    >
    <label
      ><input
        type="radio"
        class="size"
        value="Medium"
        price="20000"
        name="size"
      />Medium</label
    >
    <label
      ><input
        type="radio"
        class="size"
        value="Large"
        price="22000"
        name="size"
      />Large</label
    여기에 price 항목 추가해주세요.
    <label><input type="radio" name="dough" value="씬"    price="18000"/>씬</label>
    <label><input type="radio" name="dough" value="고구마"  price="18000"/>고구마</label>
    <label><input type="radio" name="dough" value="치즈"  price="18000"/>치즈</label>

    <h3>토핑</h3>
    <label><input type="checkbox" name="topping"  price="18000" />감자</label>
    <label><input type="checkbox" name="topping" price="18000" />고구마</label>
    <label><input type="checkbox" name="topping" price="18000" />치즈</label>
    <label><input type="checkbox" name="topping"  price="18000" />베이컨</label>
    <label><input type="checkbox" name="topping"  price="18000" />옥수수</label>


function bind () {
  const order = document
    .querySelector('#order')
    .addEventListener('click', function (event) {
      const result = document.querySelector('#result')

      // 이따 출력용이라서 뺴둠
      const size = document.querySelector('input[name="size"]:checked')
      const _size = parseInt(size.getAttribute('price'))
      // 가격 계산을 위한 코드
      //    이거는 체크박스라서 그런거임

      const pizza = document.querySelector('#pizza')
      // 이거는 피자 종류 찾아가기
      const dough = document.querySelector('input[name="dough"]:checked')

      const topping = document.querySelectorAll('input[name="topping"]:checked')

      //제대로 생각도 못해밨는데 전체에서 요소를 꺼내서 찾아야함
      // 백틱으로 전부 다쓸꺼임
      // result.innerText=`선택한 피자는 ${pizza.value}피자입니다`
      // log(size .value)
      let toppingText = ''
      let topping_price=0
      for (let i = 0; i < topping.length; i++) {
        // for문안에서 토핑 가격 합산 코드도 합산
        toppingText += topping[i].getAttribute('topping') + ' '
        const _topping = parseInt(topping[i].getAttribute('price'))
        //NodeList라서 요소 i를 사용함
      }
      //   버튼을 눌렀을때 선택한 토핑을 출력하는 방법.

      result.innerText = ` 피자: ${pizza.value} 사이즈: ${size.value} 토핑: ${toppingText}
    도우: ${dough.value} `
    })
}

//parseInt로 묶어서 value를 잡은 다음에 계산 수행.

/*

html 코드에서 price 항목 추가후, 전체적으로 추가

size 항목에서 price 가져오는법  cosnt sieze= checkd.getAttribute('price')// 선택된것 중에 항목이
price인거 나머지도 이렇게 가져오면 될거 같고, 여기서 pareInt로 감싸서 문자형-> 숫자로 변환 수행



<label
      ><input
        type="radio"
        class="size"
        value="Small"
        price="18000"
        name="size"
      />Small</label
    >
    <label
      ><input
        type="radio"
        class="size"
        value="Medium"
        price="20000"
        name="size"
      />Medium</label
    >
    <label
      ><input
        type="radio"
        class="size"
        value="Large"
        price="22000"
        name="size"
      />Large</label
    여기에 price 항목 추가해주세요.
    <label><input type="radio" name="dough" value="씬"    price="18000"/>씬</label>
    <label><input type="radio" name="dough" value="고구마"  price="18000"/>고구마</label>
    <label><input type="radio" name="dough" value="치즈"  price="18000"/>치즈</label>

    <h3>토핑</h3>
    <label><input type="checkbox" name="topping"  price="18000" />감자</label>
    <label><input type="checkbox" name="topping" price="18000" />고구마</label>
    <label><input type="checkbox" name="topping" price="18000" />치즈</label>
    <label><input type="checkbox" name="topping"  price="18000" />베이컨</label>
    <label><input type="checkbox" name="topping"  price="18000" />옥수수</label>


*/
