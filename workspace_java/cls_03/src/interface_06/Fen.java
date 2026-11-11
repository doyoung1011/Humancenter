package interface_06;

public abstract class Fen implements RemoteControl {

	@Override
	public void powerOn() {
		System.out.println("¼±Ç³±â ÄÑ±â");

	}

	@Override
	public void powerOff() {
		System.out.println("¼±Ç³±â ²ô±â");

	}

}
