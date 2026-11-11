package webservice;

import java.util.ArrayList;
import java.util.List;

public class TotalExam {

	public static void main(String[] args) {
		
		//데이터를 생산하는 곳: DAO 
		EmpDAO empDAO = new EmpDAOImpl();
        
		List<Integer> list = new ArrayList<Integer>();
		list.add(1111);
		list.add(2222);
		list.add(3333);
		list.add(4444);
		list.add(5555);
		//데이터를 생산하는 곳: DAO 
		
		//서비스 파트
		List<Integer> result = new ArrayList<Integer>();
		for (int i = 0; i < list.size(); i++) {
			if ((int) list.get(i) > 3000) {
				result.add(list.get(i));
			}
		}
        //문자열을 담는거, 메모리 낭비를 줄여진다.
		
		// jsp
		StringBuffer sb = new StringBuffer();

		for (int empno : result) {
			sb.append("<div>" + empno + "/<div>\n");

		}
		String html = sb.toString();
        
		//Servlet
		System.out.println(html); //서버

	}

}
