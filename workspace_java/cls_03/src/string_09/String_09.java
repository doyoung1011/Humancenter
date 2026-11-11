package string_09;

public class String_09 {

	public static void main(String[] args) {
		String s = "¿µÀÏÀÌ»ï»ç¿ÀÀ°Ä¥ÆÈ±¸»ï»ç";

		char c = s.charAt(3);
		System.out.println(c);

		System.out.println(s.length());

		int i = s.indexOf("»ï»ç");
		System.out.println(i);

		int i2 = s.lastIndexOf("»ï»ç");
		System.out.println(i2);

		// indexOf¸¦ »ç¿ëÇÏÁö ¾Ê°í ±¸ÇöÇÏ½Ã¿À.

		String email = "ydy7071@gmail.com";
		int chk_goal = 0; // °ñ¹ğÀÌ
		int chk_jum = 0;
		for (int j = 0; j < email.length(); j++) {
			if (email.charAt(j) == '@') {
				chk_goal++;
			} else if (email.charAt(j) == '.') {
				chk_jum++;
			}
		}
		
		if (chk_goal == 1 && chk_jum >= 1) {
		    System.out.println("ÀÌ¸ŞÀÏÀÔ´Ï´Ù.");
		}
		///////////

		String s2 = s.replace("»ï»ç", "34");
		System.out.println(s);
		System.out.println(s2);

		s2 = s.substring(5, 8);
		System.out.println(s2);

		s2 = s.substring(5);
		System.out.println();

		String[] s3 = s.split("»ï");
		for (String a : s3) {
			System.out.println(a);
 
		}
		double r = Math.random();
		System.out.println(r);

	}

}
