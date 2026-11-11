package melone_02;

public class Phone {
    //필드

	final String number;
    boolean power;
    Song ring;
	//생성자
    Phone(String number){
    	this.number=number;
    	this.power=false;
    	this.ring=new Song("기본벨소리다","블랙베리");
    	//메소드	
    }
     boolean call(String number){
    	if(Math.random()>0.5) {
    		System.out.println("전화 연결 성공"+number);
    		return true;
    	}else {
    		System.out.println("연결 실패");
    		return false;
    	}
 
    }
    void recieve() {
    	System.out.println("누구거덩?");
    }
    void message(String number,String text) {
    	System.out.println(number+"번호로"+text+"라고 보냈습니다!");
    }
    void ring() {
    	//전화벨 출력
       this.ring.play();
    }
    void ringTone(Song song) {
    	this.ring=song;
    }
	public boolean isPower() {
		return power;
	}
	public void setPower(boolean power) {
		this.power = power;
	}
	public Song getRing() {
		return ring;
	}
	public void setRing(Song ring) {
		this.ring = ring;
	}
	public String getNumber() {
		return number;
	}
   
	
}
