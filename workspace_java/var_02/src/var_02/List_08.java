package var_02;

import java.util.ArrayList;
import java.util.List;

public class List_08 {

	public static void main(String[] args) {
        //선언
		ArrayList list=new ArrayList();
		
		// 추가
		list.add(1);
		list.add("글씨");
		list.add(true);
		
		//꺼내기
		System.out.println(list.get(0));
		
		//크기
		System.out.println(list.size());
		
		for(int i=0; i<list.size();i++) {
			System.out.println(list.get(i));
		}
		for(Object obj:list) {
			System.out.println(obj);
		}
		
		int a=(int)list.get(0);
		//제네릭: 타입을 한정 시킬수 있다.
		ArrayList<String>list2=new ArrayList<String>();
		list2.add("문자열");
		
		String b=(String)list.get(1);
		String c=list2.get(0);
		
		List list3=new ArrayList();
	}

}
