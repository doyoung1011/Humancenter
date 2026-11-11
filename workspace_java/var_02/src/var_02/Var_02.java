package var_02;

public class Var_02 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//한줄
		/*
		 여러줄 주석 혹은 범위 주석
		 */
		
		System.out.println("hello world");
		
		int age=26;
		System.out.println(age);
		
//		2번
		
		String a="운전면허가 있다 없다";
		System.out.println(a);
		
		boolean yn=true;
		
		
		
		
		
		
//		참 거짓을 출력하라는 거임
		
		
		
//		문제 3
//		
		double area=3.3;
		double area_5=(5*area);
		System.out.println(area_5+"제곱미터 입니다");
		
//		문제 4
		
		int x=3;
		int y=4;
		
		boolean isBig=x>y;
		System.out.println("x>y의 결과는"+isBig+"입니다");
		
//		문제 5
		
		int total=78500;
		int human=3; // n빵 할 인원수 
		int man=10000;
		
		
		double man_money; // 만원단위 낼 돈
		
		int n_money= (total/human);  // n빵(만원단위) 했을떄 금액계산
		
		man_money=n_money/man;
		
	    System.out.println((total/human)-man_money);
		
		System.out.println(man_money);
				
		
		System.out.println(n_money+"원 입니다");
		
	
		System.out.println(n_money+"입니다");
		
		
//		강사님 버전!
        System.out.println("============");
		int totals=78500;
		int members=3;
		int member=total/members;
		
		System.out.println(member);
		
		int money1=(member/10000)*10000;
		
		System.out.println(money1);
		
		int money2=total-(money1*(members-1));
		
		System.out.println(money2);
		
		
         		

		
		
		
		
//		문제 6
		
		String left="국밥";
		String right="돈까스";
		
		String temp=left;
		left=right;
		right=temp;
		
		System.out.println(left);
		System.out.println(right);
		
		
		
		int i1=10;
		long i2=i1; // 생략가능
		i2=i1;
		
		i1=(int)i2;
		
		i2=200000000L;
		i1=(int)i2;
		System.out.println(i1);
		
		float ff1=1.23f;
		double ff2=ff1;
		ff1=(float)ff2;
		
		int i3=2100000000;
		int i4=i3*3;
		
		System.out.println(i4);
		
		int i5=10;
		double i6=i5;
		
		int i7=33;
		int i8=10;
		
		double i9=i7/i8;
		
		System.out.println(i9);
		
		double d2 = 10 /4;
		System.out.println(d2);
		
		double d3=10.0/4;
		System.out.println(d3);
		
		double d4= (double)10/4;
		
		String s2="123";
//		int ii1=int(s2); // 지원하지 않음
		
		int il1=Integer.parseInt(s2);
		
		
		
		
		
		
		
		
		
	}

}
