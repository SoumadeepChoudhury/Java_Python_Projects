package soumadeep;

public class Year2017_Q8 {
	void check(String str, char ch) {
		int f = 0;
		for (int i = 0; i < str.length(); i++)
			if (str.charAt(i) == ch)
				f++;
		System.out.println("Number of " + ch + " present is= " + f);
	}

	void check(String s1) {
		s1 = s1.toLowerCase();
		for (int i = 0; i < s1.length(); i++) {
			if (s1.charAt(i) == 'a' || s1.charAt(i) == 'e' || s1.charAt(i) == 'i' || s1.charAt(i) == 'o'
					|| s1.charAt(i) == 'u')
				System.out.print(s1.charAt(i) + " ");
		}
	}

	public static void main(String[] args) {

		Year2017_Q8 ob = new Year2017_Q8();
		ob.check("success", 's');
		ob.check("computer");
	}

}
