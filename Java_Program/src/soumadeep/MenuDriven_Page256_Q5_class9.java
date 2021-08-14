package soumadeep;

import java.util.Scanner;

public class MenuDriven_Page256_Q5_class9 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.println("1. S=1/4+1/8+1/12....n terms");
		System.out.println("2. S=1/1!-2/2!+3/3!....n terms");
		System.out.print("Enter choice 1/2: ");
		int c = sc.nextInt();
		switch (c) {
		case 1:
			System.out.print("Enter number of terms: ");
			int n = sc.nextInt();

			double s = 0.0d;
			int x = 4;
			for (int i = 1; i <= n; i++) {
				s += 1.0 / x;
				x += 4;
			}

			System.out.print("Value of S= " + s);
			break;
		case 2:
			System.out.print("Enter number of terms: ");
			int m = sc.nextInt();
			double sum = 0.0d;
			int f = 1;
			double t = 0;
			for (int i = 1; i <= m; i++) {
				f *= i;
				t = (i % 2 == 0) ? ((-i * 1.0) / f) : ((i * 1.0) / f);
				sum += t;
			}
			System.out.print("Value of S= " + sum);
			break;
		default:
			System.out.print("Invalid Choice");
		}

	}

}
