package var_03;

public class Say {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("hello world");
		
		
		
		int[]b={7,12,8,5};
		int[]c=new int[b.length+1];
		
		for(int i=0;i<b.length;i++) {
			c[i]=b[i];
			
		}
		c[c.length-1]=3;
		
		for(int i=0;i<c.length;i++) {
			System.out.print(c[i]);
		}
		// 처음에다가 1 끼워 넣기
		
		
		System.out.println("===");
		int[]d=new int[c.length+1]; // 배열 d는 한칸 크게 크게 선언
		d[0]=1; // 냅다 끼워넣기(처음에 넣는거니까)
		for(int i=0;i<c.length;i++) {
			d[i+1]=c[i]; //이게 한칸 씩 뒤로 미는것임
		}
		for(int i=0;i<d.length;i++) {
			System.out.print(d[i]);
		}
		
		
//		int []array= {11,5,8,6,9};
//		
//	    for(int i=0;i<array.length;i++) {
//	    	if(array[0]>array[1]) {
//	    	   continue;
//	    	}else {
//	    		array[0]=array[5];
//	    	}
//	    	System.out.println("==============");
//	    	System.out.print(array[i]);
//	    }
//		

		
		
		
		//d[0]=1
		//d[1]=7, c[2]
		
		
		
		
		//맨 마지막에다가 3을 끼워 넣어봅시다.
		//c[0]=b[0]
		//c[1]=b[1]
		
		
		

	}

}
