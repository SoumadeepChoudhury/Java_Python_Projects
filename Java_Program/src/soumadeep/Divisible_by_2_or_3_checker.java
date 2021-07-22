package soumadeep;

import java.util.Scanner;

public class Divisible_by_2_or_3_checker {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter 3 to 6 digit ");
		String n = sc.next();
		if (n.length() < 3 || n.length() > 6)
			System.out.print("Enter proper data");
		else {
			System.out.println("Digits divisible by 2 \t Digits Divisible by 3");
			System.out.println("~~~~~~~~~~~~~~~~~~~~~ \t ~~~~~~~~~~~~~~~~~~~~~");
			char c[] = n.toCharArray();
			for (int i = 0; i < c.length; i++) {
				if (Integer.parseInt("" + c[i]) % 2 == 0)
					System.out.println(c[i]);
				if (Integer.parseInt("" + c[i]) % 3 == 0)
					System.out.println("\t\t\t\t" + c[i]);
			}
		}
	}

}
