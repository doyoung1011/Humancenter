package game_04;


//final: 클래스의 경우 상속 불가.
public class Champ {

	void attack() {
		System.out.println("기본 공격합니다.");
	}
    
	//final: 메소드의 경우 오버라이드 금지!
	
	void move() {
		System.out.println("이동합니다.");
	}

	void skill(String key) {
		if (key.equals("R")) {
			System.out.println("궁극기를 사용합니다.");
		} else if (key.equals("F")) {
			System.out.println("점멸을 사용합니다.");
		}
	}

	void recall() {
		System.out.println("귀환 합니다.");
	}

}
