package var_02;

public class Type_03 {

	public static void main(String[] args) {

		// StringBuffer
		StringBuffer sb = new StringBuffer();
		sb.append("A");
		sb.append("B");
		sb.append("C");

		// StringBufferfmf String으로 변환하는 방법
		String s1 = sb.toString();

		// 배열
//		int a[]; // c언어 스타일
		int[] a2; // java스타일
		int[][] a3; // 2차원 배열

		// null
		// null은 참조가 없는 상태
		// 기본타입에는 null을 넣을수 없다아
		// 참조 타입에는 null을 넣을 수 있다.
		// 배열 선언의 첫 번쨰 방법
		int[] a4 = new int[30];
		a4[0] = 10;

		System.out.println(a4);

		String[] str = new String[6];
		// 배열 선언 두 번 쨰 방법
		// 값을 알고 있을 떄
		int[] a5 = new int[] { 1, 2, 3, 4 };

		System.out.println(a5[3]);

		int[] a6 = { 1, 2, 3, 4 };
		System.out.println("a6.length" + a6.length);

		int[] a = { 1, 2, 3, 4, 5 };

		for (int i = 0; i < a.length; i++) {
			System.out.println(a[i]);
		}
		
		//2차원 배열
		int[]floor=new int[10];
		int[]floor2=new int[10];
		int[]floor3=new int[10];
		
		int[][]백자=new int[3][10];
		System.out.println(백자);
		System.out.println(백자.length);
		System.out.println(백자[0].length);
		System.out.println(백자[0][0]);
	    //백자 2의 모든 내용 출력하기
		int[][]백자2={
				{11,12},
				{21,22,23},
				{31,32,33,34}
		};
		for(int i=0;i<백자2.length;i++) {
			for(int j=0;j<백자2[i].length;j++) {
				System.out.println(백자2[i][j]);
			}
		}
		int[]b={7,12,8,5};
		int[]c=new int[b.length];
		c[0]=b[3]; // length
		c[1]=b[2];
		c[2]=b[1];
		c[3]=b[0];
		
		for(int i=0;i<b.length;i++) {
			c[i]=b[b.length-1-i]; // 더해서 3이니까
		}
		for(int i=0;i<c.length;i
				++) {
			System.out.println(c[i]);
		}
		//b의 마지막에 3을 추가한 배열 d를 만들어서 출력하시오
		
		//1. b의 마지막에 3을 추가한다. 
		//2. 출력한다.
		//int[]b={7,12,8,5};
 		int[]d=new int[b.length+1]; // 이러면 배열 선언은 완료.
 		System.out.println("========");
 		for(int i=0;i<b.length;i++) {
 			d[i]=b[i];
 		}
 		d[d.length-1]=3;
 		
 		for(int i=0;i<d.length;i++) {
 			System.out.println(d[i]);
 		}
 		
 		//맨처음에 넣어보기 3을
 		
 		
 		
 		int[]e=new int[b.length+1];
 		e[0]=3;
 		
 		for(int i=0;i<b.length;i++) {
 			e[i+1]=b[i];
 		}
 		
 		int count=0;
 		// 홀수의 개수는? 
 		for(int i=0;i<e.length;i++) {
 			if(e[i]%2==1) {
 				count++;
 			}
 		}
// 		System.err.println("=================");
// 		System.err.println("홀수 개수: "+count);
 		
 		System.out.println("============");
 		int index=2;
 		int value=3;
 		int[]f=new int[b.length+1];
 		for(int i=0;i<f.length;i++) {
 			if(i== index) {
 				f[i]=value;
 				
 			}else if(i<index) {
 				f[i]=b[i];
 			}else if(i>index) {
 				f[i]=b[i-1];
 			}
 		}
 		for(int i=0; i<f.length;i++ ) {
 			System.out.println(f[i]);
 		}
 		
 		// 구구단 출력하기
 		// i*j
 		// 1*1 
 		// 1*2
 		// 1*3
 		// 1*4
 		System.out.println("==========");
 		for(int i=2;i<=9;i++) {
 			for(int j=1;j<=9;j++) {
 			System.out.println("구구단"+(j*i));	
 			}
 		}
 		// 
 		
 		
 		
 		
 	    
 	
 	
 		
 		

 		
 	
 		

 		
 		//d[0]=b[0] 7
 		//d[1]=b[1] 12
 		//d[2]=b[2] 8
 		//d[3]=b[3] 5
 		//d[4]=3 
// 		for(int i=0;i<b.length+1;i++) {
// 			d[i]=b[b.length];
// 		}
 		
       // b의 맨 처음에 3을 추가한 배열 e를 만들어서 출력하기
 	   // e 중에서 홀수의 개수는 몇개인가.
 		
 		// 주말 숙제
 		// 임시 비밀 번호만들기 10자리 배열 10자리.
 		//영어, 숫자 포함,소문자 하나, 
 		// hint: 아스키 코드, char
 		
 		String []pw=new String[10];
 		
 		int upper_count=0; // 대문자 카운트
 		int lower_count=0; // 소문자 카운트
 		int num_count=0; // 숫자 카운트
 		
 		//최종적으로 10번 반복하기
 		// 대/소문자를 랜덤으로 뽑아서 붙이기
 		
 		
 		
 	    
 		
 		
 		
 		
 		
 		
 		
 		
 		
 		
 			
 		
 		
		
		
	}

}
