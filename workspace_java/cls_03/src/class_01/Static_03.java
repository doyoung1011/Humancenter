package class_01;

public class Static_03 {
	static double PI=3.14;
	String name;
	
	
	//상수: static final
	// static: 선발대 개념
	static final String 주민번호="1235-5";
	
	static final String OK="E1";
	// static
	//생성하지 않고 바로 사용할 수 있는 것
	// 모든 클래스가 공통적ㅇ로 가지고 있다.
	static double getPI() {
//		name="anc";
		return PI;
		
		
	}
	void setPI(double p) {
		PI=p;
	}
	Static_03(){
		PI=3.14;
	}

}
