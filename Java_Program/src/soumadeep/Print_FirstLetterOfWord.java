package soumadeep;

import java.util.Scanner;

public class Print_FirstLetterOfWord {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter sentence: ");
		String s = sc.nextLine();
		s = " " + s;
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == 32)
				System.out.print(s.charAt(i + 1) + ". ");
		}

	}

}
