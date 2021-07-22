package soumadeep;

import java.util.Scanner;

public class Year2017_Q5 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {

		System.out.print("Enter number: ");
		int n = sc.nextInt();
		int s = 0, p = 1;
		while (n > 0) {
			int d = n % 10;
			s += d;
			p *= d;
			n /= 10;
		}
		if (s == p)
			System.out.print("Spy Number");
		else
			System.out.print("Not Spy Number");

	}

}
