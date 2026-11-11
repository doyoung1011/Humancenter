package abstract_05;

import java.util.ArrayList;
import java.util.List;

// abstract
// 부모 전용 클래스라서 new 할 수 없다.
//
public abstract class Student {
	
	List skills=new ArrayList();
	
	Student() {
		System.out.println("Student 생성자 실행");
	}
	void eat() {
		System.out.println("우걱 우걱 밥 먹는닷");
	}
	//추상 메소드.
	//실행 블럭이 있으면 안됨
	//나는 구현하지 않는다.
	//자식에게 구현을 떠넘긴다.
	
	abstract void study();
	

}
