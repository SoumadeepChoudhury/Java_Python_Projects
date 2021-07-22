package soumadeep;

import java.util.Scanner;

public class Year2016_Q6 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int m = 0, l;
		System.out.print("Enter A word: ");
		String a = sc.next();
		l = a.length() - 1;
		for (int i = 0; i < l / 2; i++) {
			if (a.charAt(i) == a.charAt(l - i))
				m++;
		}
		if (m == l / 2)
			System.out.print("Palindrome");
		else {
			if (a.charAt(0) == a.charAt(l))
				System.out.print("Special Word");
			else
				System.out.print("Neither Palindrome Nor Special Word");
		}
	}

}
