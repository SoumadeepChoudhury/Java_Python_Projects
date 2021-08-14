package soumadeep;

import java.util.Scanner;

public class Palindrome {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter String: ");
		String A = sc.next();
		int l = A.length() - 1;
		int m = 0, c = 0;
		for (int i = 0; i < A.length(); i++) {
			if (Character.toUpperCase(A.charAt(i)) == 'A' || Character.toUpperCase(A.charAt(i)) == 'E'
					|| Character.toUpperCase(A.charAt(i)) == 'I' || Character.toUpperCase(A.charAt(i)) == 'O'
					|| Character.toUpperCase(A.charAt(i)) == 'U')
				c++;
		}
		for (int i = 0; i < l / 2; i++) {
			if (A.charAt(i) == A.charAt(l - i))
				m++;
		}
		System.out.println("Number of Vowels: " + c);
		if (m == l / 2)
			System.out.print("Yes");
		else
			System.out.print("No");
	}
}
