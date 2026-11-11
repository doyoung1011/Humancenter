package var_02;

public class OP {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println("hello");
		
		int x=10;
		x++;
		System.out.println("x:"+x);
		
		++x;
		System.out.println("x: "+x);
		
		x=10;
		int y=++x;
		
		System.out.println(y);
		
		x=10;
		y=x++ + ++x;
		System.out.println(y);
		
		x=10;
		y=x++ * --x / ++x -x--;
		
		// x=10
		// 10*10 / 11-11
		
		System.out.println(y);
		
		x=10;
		y=x++ + (--x / ++x) -x--;
		
//		x=10 
//		10+(9/10)-11
		System.out.println(y);
		
		x=0;
		System.out.println(x++);
		
		double a=7.3;
		int b=0;
		System.out.println(a/b);
		
		int c=149;
//		기습 문제...! 10의 자리만 출력
		
		int n=c%100;
		
		System.out.println(n);
		
		int nn=n/10;
		
		System.out.println(nn);
		
		
		float d=0.1f;
		double e=0.1;
		boolean f=d==e;
		System.out.println(f);
		
//		소수점은 근사치로 저장됨.
		
		String s1="s1";
		String s2="s1";
		
		System.out.println(s1.equals(s2));
		
		
      // 문제 2
		
	   double bbero;
	   int orig=1200000;
	   
	   double sale=orig*0.15;
	   
	   double price=orig-sale;
	   System.out.println((price));
	   
	   
	   double v1=1000;
	   double v2=794.0;
	   
	   
//	   소수점 3번쨰 까지 출력하시오. 나누었을때
	   
	   double div=(v1/v2);
	  
	   double div3=(long)(div*1000)/1000.0;
	   
	   
	   System.out.println(div3);
	   
     // 삼항 연산자
	   
	   int score=85;
	   String grage=(score>=90)? "A학점" :"B학점";
	   System.out.println(grage);
	   
	   // 문제4
	   //90이상:A
	   //80이상:b
	   //그 외:c
	   
	   String upgrage=(score>=90)? "A학점":(score>=90 && score>=80)?"B학점":"C학점";
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	 
	   

	   
	  
	   
	   
		
		
		
		
		

	}

}
