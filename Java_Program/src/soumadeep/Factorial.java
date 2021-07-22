package soumadeep;

import java.util.Scanner;

public class Factorial {
	static Scanner sc = new Scanner(System.in);
	static int f = 1;

	// Recursion
	static int fac(int n) {

		if (n >= 1) {
			f *= n;
			fac(--n);
		}
		return f;
	}

	public static void main(String[] args) {
		System.out.print("Enter number: ");
		int n = sc.nextInt();
		System.out.print("Factorial: " + fac(n));
		// Iterative
		int f1 = 1;
		for (int i = 2; i <= n; i++) {
			f1 *= i;
		}
		System.out.print("\nFactorial: " + f1);
	}

}
