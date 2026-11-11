package game_04;

public class LoL_Exam {

	public static void main(String[] args) {

		Vi 바이 = new Vi();
		바이.move();
		바이.skill("R");

		Jax jax = new Jax();
		jax.move();

		Champ champ1 = 바이;
		Champ champ2 = jax;
		
		champ1.move();

		Auto auto = new Auto();
		auto.run(바이);
		auto.run(jax);
		
		Vi vi2=(Vi)champ1;
	
	}

}
