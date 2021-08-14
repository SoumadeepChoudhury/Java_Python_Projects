package soumadeep;

import java.util.Scanner;

public class Year2014_Q5 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter two digit number: ");
		int n = sc.nextInt();
		if (((n % 10 + n / 10) + (n % 10 * (n / 10))) == n)
			System.out.print("Special 2-digit number");
		else
			System.out.print("Not a special two digit number");
	}

}
