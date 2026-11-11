package melone_02;

public class PhoneEaxm {

	public static void main(String[] args) {
		Phone phone1 = new Phone("010-1245-5646");
		Phone phone2 = new Phone("010-2245-5646");

		phone1.setPower(true);

		Song song = new Song("좋은날", "아이유");
		// phone1의 벨소리 바꾸기
		phone1.setRing(song);

		phone1.ringTone(song);

		phone2.setPower(true);
		if (phone2.call(phone1.getNumber())) {
			phone1.ring();
			phone1.recieve();
		}
		Smartphone s1 = new Smartphone("010-4444-4444");
		Smartphone s2 = new Smartphone("112");

		if (s2.call(phone1.getNumber())) {
			s1.ring();
			s1.recieve();
		}
		s1.message(s2.getNumber(), "자니?");
		s1.search("?");

	}

	
	

}
