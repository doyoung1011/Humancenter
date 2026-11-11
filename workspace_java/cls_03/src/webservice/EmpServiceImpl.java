package webservice;

import java.util.ArrayList;
import java.util.List;

public class EmpServiceImpl implements EmpService {

	@Override
	public List getEmp() {
		EmpDAO empDAO=new EmpDAOImpl();
		
		List list=empDAO.selectEmp();
		
		List result=new ArrayList();
		for(int i=0;i<list.size();i++) {
			if((int)list.get(i)>3000) {
				result.add(list.get(i));
			}
		}
		
		
		
		return list;
	}

}
