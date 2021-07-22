package soumadeep;

import java.util.Scanner;

public class Year2018_Q6 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter a sentence in lower case: ");
		String s = sc.nextLine();
		s = " " + s;
		String new_s = "";
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == 32) {
				new_s += " " + Character.toUpperCase(s.charAt(i + 1));
				i++;
			} else
				new_s += s.charAt(i);
		}
		System.out.print(new_s.trim());
	}

}
