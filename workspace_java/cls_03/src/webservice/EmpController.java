package webservice;

import java.util.List;

public class EmpController implements Servlet {

	@Override
	public String doGet() {
		
		EmpService empService=new EmpServiceImpl();
		List list=empService.getEmp();
		
		Jsp jsp=new Jsp(); //jsp 만들고, list에다가 넣겠다 그리고 return때리겠다.
		String html=jsp.view(list);
		
//		String html="<div>ename:SCOTT</div>";
		
		return html;
		
	}

	@Override
	public String doPost() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public String doPut() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public String doDelete() {
		// TODO Auto-generated method stub
		return null;
	}

}
