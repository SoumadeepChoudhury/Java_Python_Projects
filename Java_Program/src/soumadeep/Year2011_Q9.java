package soumadeep;

import java.util.Scanner;

public class Year2011_Q9 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter choice: \n1. 0,3,8,15,24...n terms\n2. S=1/2+3/4+.....19/20. ");
		int n = sc.nextInt();
		switch (n) {
		case 1:
			System.out.print("Enter n: ");
			int n1 = sc.nextInt();
			for (int i = 1; i <= n1; i++) {
				System.out.print((i * i - 1) + ", ");
			}
			break;
		case 2:
			double S = 0.0;
			for (int i = 2; i <= 20; i += 2)
				S += ((i - 1) * 1.0) / 2;
			System.out.print("Sum: " + S);
			break;
		default:
			System.out.print("Invalid Choice");
		}

	}

}
