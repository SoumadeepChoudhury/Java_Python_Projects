package soumadeep;

import java.util.Scanner;

public class TestPaper2_Q8 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int f = 0;
		System.out.print("Enter String: ");
		String s = sc.nextLine();
		s = s.toUpperCase();
		System.out.println("Characters\tFrequency");
		for (int i = 65; i <= 90; i++) {
			f = 0;
			for (int j = 0; j < s.length(); j++) {
				if (s.charAt(j) == (char) i)
					f++;
			}
			if (f > 0)
				System.out.println((char) i + "\t\t" + f);
		}

	}

}
