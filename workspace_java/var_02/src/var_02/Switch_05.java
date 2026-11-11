package var_02;

import java.util.Scanner;

public class Switch_05 {

	public static void main(String[] args) {
		
		Scanner scan=new Scanner(System.in);
		System.out.print("숫자를 입력하시오:");
		int a=scan.nextInt();
		System.out.println(a);
		
		switch (a) {
		case 1:
			System.out.println("a는 1이다.");
			break;

		default:
			System.out.println("그외");
		}
		
		
		switch(a) {
		case 12:
		case 1:
		case 2:
			System.out.println("겨울");
			break;
		case 3:
		case 4:
		case 5:
			System.out.println("봄");
			break;
		case 6:
		case 7:
		case 8:
			System.out.println("여름");
			break;
		case 9:
		case 10:
		case 11:
			System.out.println("가을");
			break;
		
		}
		
		
	
	}

}
