package soumadeep;

import java.util.Scanner;

public class GCD_HCF {
	static Scanner sc = new Scanner(System.in);
	static int a1, b1, c = 1, gcd;

	public static void main(String[] args) {
		int a = 24, b = 6;
		int n1, n2;
		if (a > b) {
			n1 = a;
			n2 = b;
		} else {
			n1 = b;
			n2 = a;
		}
		while (n1 % n2 != 0) {
			n1 = n2;
			n2 = n1 % n2;
		}

		System.out.print("GCD: " + n2);

		// recursion

		System.out.print("Enter no. :");
		a1 = sc.nextInt();
		b1 = sc.nextInt();
		hcf(1);
		System.out.print(gcd);
	}

	static void hcf(int x) {
		if (x < Math.max(a1, b1)) {
			if (a1 % x == 0 && b1 % x == 0)
				gcd = x;
			hcf(++x);
		}

	}

}
