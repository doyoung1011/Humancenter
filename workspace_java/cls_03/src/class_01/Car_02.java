package class_01;

public class Car_02 {
	
	//필드(공용, 전역 변수)
	// 변수 선언만 가능하다.
	// 선언 하면서 동시에 초기화 가능!
	String company="비엠따르릉";
	String model="m340i";
	int maxSpeed=260;
	
	int year;
	
	int speed;
	// 필드 영역에서는 실행(행동) 할 수 없다.
	// speed=10; -> speed의 값을 10으로 바꾸는 행동 불가.
	
	boolean power;
	
	
	/*
      메소드 선언      
      리턴타입 메소드명(전달인자){}
      
	 */
	
	void powerOn() {
		power=true;
	}
	void powerOff() {
		power=false;
	}
	
	
	void setSpeed(int s) {
		System.out.println(s);
       
		if(s>=maxSpeed) {
		    s=maxSpeed;
		}
		speed=s;
	
		
	}
	/*
	 * 속도 즉 필드의 speed를 돌려준다 
	 */
	
	int getSpeed() {
		return speed;
	}
	int getSpeed(int s) {
		System.out.println();
		System.out.println(s);
		return speed;
	}
	
	//overloading 오버로딩
	//전달인자 타입의 개수,순서
	//메소드명을 동일하게 할 수 있는 것
	//전달인자 자료형이 정확히 동일한 것, 우선순위 높음.
	
	//전달인자 자료형이 정확히 동일한 것이 우선순위 높음
	// 그다음에 자동형변환으로 들어갈 수 있는 것.
	
//	int plus(int x,int y) {
//		System.out.println("int plus(int x,int y)");
//		return x+y;
//	}
	int plus(int x) {
		return x+x;
	}
	
	int minus(int x,int y) {
		return x-y;
	}
	
	double plus(double x,double y) {
		System.out.println("dobule plus(int x,int y)");
		return x+y;
	}
	
	
	//생성자
	//생성자를 선언하지 않으면 무조건 기본 생성자가 자동완성됨.
	Car_02(){
		System.out.println("생성자 실행");
	}
	Car_02(String m,int y,boolean p){
		model=m;
		year=y;
		power=p;
		
	}
	
	Car_02(String m){
		this(m,2026,false);
		
//		model=m;
//		year=2026;
//		power=false;
		System.out.println();
		
		
	}
	void setYear(int year) {
		this.year=year;
	}
	
	
	
	
	
}
