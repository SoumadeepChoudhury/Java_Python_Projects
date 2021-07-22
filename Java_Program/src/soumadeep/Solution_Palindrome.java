package soumadeep;

import java.util.Scanner;

public class Solution_Palindrome {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter String: ");
		String A = sc.next();
		int l = A.length() - 1;
		int m = 0;
		for (int i = 0; i < l / 2; i++) {
			if (A.charAt(i) == A.charAt(l - i))
				m++;
		}
		if (m == l / 2)
			System.out.print("Yes");
		else
			System.out.print("No");

	}
}