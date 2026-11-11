package class_01;

public class CarExam {

	public static void main(String[] args) {
		int a;
//		System.out.println(a);
	 Car_02	c1=new Car_02();
	 Car_02 c2=new Car_02();
	 
	 int ms=c1.maxSpeed;
	 System.out.println(ms);
	 
	 //초기화 하지 않은 경우
	 //0,false,null로 초기화 된다.
	 
	 
	 int s=c1.speed;
	 System.out.println(s);
	 
	 c1.speed=400;
	 c2.speed=399;
	 System.out.println(c1.speed);
	 
	 System.out.println(c1.power);
	 c1.powerOn();
	 
	 c1.plus(1,2);
	}
	//숫자를 적어서 주면
	// speed에 반영한다
	// 단, 최고속도 이상을 받으면 최고 속도로 고정
	
	
	

}
