package var_02;

public class While_07 {

	public static void main(String[] args) {
		// while이긴 하지만
		// for문으로 주사위 한번더

		// 2개 중복없이
		int i = 3;
		while (i < 10) {
			System.out.println(i);
			i++;
		}
//		i=3;
		do {
			System.out.println(i);
		} while (i < 10);

		// if에는 홀수만 사용하기
		System.out.println("=================");
		i = 0;
		while (i < 10) {
			i++;
			if (i % 2 == 1) {
				continue;
			}
			System.out.println(i);

		}

		System.out.println("============");

//		int sum=0;
//        //주사위 갯수 2개, 랜덤으로 뿅뿅 나옴
//		for(int a=1;a<=2;a++) {
//		int dice=(int)(Math.random()*6)+1;
//		
//		sum+=dice;
//		}
//		System.out.println(sum);

//		int sum=0;
//		
//		int dice=(int)(Math.random()*6)+1;
//		int dice2=(int)(Math.random()*6)+1;

//		int sum=0;
//
//		int dice=(int)(Math.random()*6)+1;
//		int dice2=(int)(Math.random()*6)+1;
////
////		sum+=dice+dice2;
////		System.out.println(sum);
//		
//		if(dice==dice2) {
//			System.out.println("값이 동일합니다!");
//		}else {
//			System.out.println("값이 다릅니다...");
//		}
//		System.out.println("첫번째 주사위:"+dice+" 두번쨰 주사위"+dice2);

	}

}
