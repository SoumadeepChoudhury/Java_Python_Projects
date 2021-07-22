package soumadeep;

import java.util.Scanner;

public class Year2013_Q9 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter choice: \n1. Composite or Not. \n2. Smallest Digit. ");
		int n = sc.nextInt();

		switch (n) {
		case 1:
			System.out.print("Enter number: ");
			int n1 = sc.nextInt();
			int c = 0;
			for (int i = 2; i < n1; i++)
				if (n1 % i == 0)
					c++;
			if (c > 0)
				System.out.print("Composite Number");
			else
				System.out.print("Not Composite Number");
			break;
		case 2:
			System.out.print("Enter number: ");
			int x = sc.nextInt();
			int p = x % 10;
			while (x > 0) {
				int d = x % 10;
				if (d < p)
					p = d;
				x /= 10;
			}
			System.out.print("Smallest digit: " + p);
			break;
		default:
			System.out.print("Invalid Choice");
		}

	}

}
