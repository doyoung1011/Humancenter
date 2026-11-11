package melone_02;

public class MelonExam {

	public static void main(String[] args) {
	  
		Melon melon=new Melon();
		
		Song s1=new Song("with", "리센느");
		boolean result=melon.addSong(s1);
		
		if(result) {
			System.out.println("s1이 정상적 추가되었습니다.");
		}else {
			System.out.println("추가되지 않았습니다. 관리자 문의 시급");
		}
		
		Song s2=new Song("꿈꾸던 어른이 되었나요??", "머무르");
		melon.addSong(s2);
		

		melon.showList(10);

	}

}
