package soumadeep;

import java.util.Scanner;

public class Year2013_Q5 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter 10 digit ISBN: ");
		String s = sc.next();
		if (s.length() != 10)
			System.out.print("Illegal ISBN");
		else {
			double s1 = 0;
			for (int i = 0; i < s.length(); i++) {
				s1 += (i + 1) * Integer.parseInt("" + s.charAt(i));
			}
			if (s1 % 11 == 0)
				System.out.print("Legal ISBN");
			else
				System.out.print("Illegal ISBN");
		}
	}

}
