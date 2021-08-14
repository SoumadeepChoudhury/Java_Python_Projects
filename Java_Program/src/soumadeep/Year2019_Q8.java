package soumadeep;

import java.util.Scanner;

public class Year2019_Q8 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter sentence: ");
		String s = sc.nextLine();
		s = s.toUpperCase();
		int f = 0;
		s = " " + s;
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == 32) {
				if (s.charAt(i + 1) == 'A')
					f++;
			}
		}
		System.out.println("Total Number of words starting with letter 'A'= " + f);
	}

}
