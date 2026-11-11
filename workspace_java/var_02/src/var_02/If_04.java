package var_02;

public class If_04 {

	public static void main(String[] args) {

		if (3 < 2) {
			System.out.println("참");
		} else {
			System.out.println("거짓");
		}

		int a = 3;
		// 기습 문제
		// a를 홀,짞으로 출력하시오

		if (a % 2 == 0) {
			System.out.println("짝");
		} else {
			System.out.println("홀");
		}

		double rand = Math.random();
		int min = 3;
		int max = 7;

		// 0~7까지만 나오게성공
		// 0~0.9999나옹는거를 >>>> 0~7.999까지 나오게 하기
//		double result=(int)(rand*(min+1));
		// 이러면 0부터 3까지 나옴
		// 그렇다면

		double result = (int) (rand * (max - min + 1) + min);

		System.out.println(result);
		// rand의 결과가 min-max로 나오게 하시오.

		int num = 3;
		int num2 = 0;
		if (num2 != 0) {
			if (num2 != 0 && num / num2 == 0) {
				System.out.println("참");
			} else {
				System.out.println("거짓");
			}

		}

	}
}
