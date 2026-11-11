package melone_02;

public class Song {
	
	String title;	//제목
	String singer;  //가수
	String album;   //앨범명
    int rank;       //순위 
	long like;      //좋아요 수
 	String albumArtUrl; //앨범아트 이미지 경로
	boolean userYN; //사용 여부
	
	// 생성자
	// 제목이랑 가수

	
	public Song(String title,String singer){
		this.title=title;
		this.singer=singer;
		
		this.album=title; //싱글앨범일 경우
		this.rank=-1;
		this.like=0;
		this.albumArtUrl="기본이미지";
		this.userYN=true;
	}
	// 메소드
	// 재생,다운로드,좋아요 수정.
	public void play() {
		System.out.println(this.title+"을 재생합니다");
	}
	String download() {
		return this.title+"다운로드 주소";
	}
	
	/*
	 * 좋아요 숫자를 변경한다. 
	 * 좋아요를 눌렀을 떄 1 증가
	 * 좋아요를 뺐을 떄 1 감소
	 * @param boolean
	 * true: 좋아요 눌렀을 떄
	 * false: 좋아요 뻈을때
	 * @return long 좋아요 수
	 */
	long  updateLike(boolean action) {
		if(action) {
			this.like++;
		}else {
			this.like--;
		}
		return this.like;
	}
	
	
}
