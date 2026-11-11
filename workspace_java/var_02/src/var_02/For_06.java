package var_02;

public class For_06 {

	public static void main(String[] args) {

		// for문의 형식

		for (int i = 0; i < 10; i++) {
			System.out.println(i);
		}

		int result = 0;
		for (int j = 0; j <= 10; j++) {
			result += j;

		}
		System.out.println(result);
		System.out.println("=============================");

		// 주사위 2개를 굴려서 나올수 있는 모든 조합을 출력하시오.
		// 2개를 굴려서 나올 수 있는 모든 조합을 합 별로 출력하기
		// 단 중복 x

		int rand = (int) (Math.random() * 6) + 1;

		int s = 0;
		for (int k = 2; k <= 12; k++) {
			for (int i = 1; i <= 6; i++) {
				for (int j = 1; j <= 6; j++) {
					if (i + j == k)
						System.out.printf("[%d,%d]", i, j);
				}

			}

		}
		// 향상된 for문
		int[]score= {1,2,3,4,5};
		for (int a:score) {
			System.out.println(a);
		}
	
		
	}
}