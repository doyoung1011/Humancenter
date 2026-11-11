package melone_02;

//this는 메모리에 올라간 나
//extends: 상속, private를 제외한 모든 요소를 상속받을 수 있다.

public class Smartphone extends Phone {
	Smartphone(String number){
		super(number);
		
		System.out.println(this.number);
		ring();
//		System.out.println(this.power);
	}
	
	void openStore() {
		System.out.println("어플 목록이 나옵니다.");
	}
    String search(String keyword) {
		System.out.println("키워드 검색 중입니다.");
		
		super.message("1", "text");
		
		return keyword+"검색 결과 페이지";
	}
    @Override	
    void message(String number,String text) {
    	System.out.println("1"+text);
    }
    

}
