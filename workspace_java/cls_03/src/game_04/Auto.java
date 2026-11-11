package game_04;

public class Auto {
    
	void run(Champ champ) {
		champ.attack();
		champ.move();
		champ.skill("F");
		champ.skill("R");
		champ.recall();
	}
}
