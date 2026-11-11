package var_02;

import java.util.HashMap;
import java.util.Map;


public class Map_09 {

	public static void main(String[] args) {
		HashMap map=new HashMap();
		
		map.put("key", "v1");
		map.put("k2", 2);
		
		System.out.println(map.get("key"));
		
		String s =(String) map.get("k1");
		
		// 없으면 null
		System.out.println(map.get("key100"));
		
//		Map<String,Integer> map2 =new HashMap<String,Integer>;
//		map2.put("k1",1);
//		int a=map2.get("k1");
		
		//멜론 차트 1~3까지를 저장해서 관리할거임
		//한 곡당 가수명,제목으로 저장
		//멜론을 만들어야하거덩
		
		Map<String,String> song=new HashMap<String,String>();
		song.put("제목","with");
		song.put("가수","리센느");
		
		
		//final
		int x=10;
		x=20;
		
		final int y=20;
		
		
		
		

	}

}
