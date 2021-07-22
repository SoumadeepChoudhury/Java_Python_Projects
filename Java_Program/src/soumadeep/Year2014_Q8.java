package soumadeep;

import java.util.Scanner;

public class Year2014_Q8 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("1. Term Deposit \n2. Recurring Deposit \nEnter choice: ");
		int ch = sc.nextInt();
		switch (ch) {
		case 1:
			System.out.print("Principal: ");
			double P = sc.nextDouble();
			System.out.print("Rate of Interest: ");
			double r = sc.nextDouble();
			System.out.print("Enter Time peiod: ");
			int n = sc.nextInt();
			double A = P * Math.pow(1 + r / 100, n);
			System.out.print("Maturity Value: " + A);
			break;
		case 2:
			System.out.print("Principal: ");
			double P1 = sc.nextDouble();
			System.out.print("Rate of Interest: ");
			double r1 = sc.nextDouble();
			System.out.print("Enter Time peiod: ");
			int n1 = sc.nextInt();
			double a = (P1 * n1) + ((P1 * n1 * (n1 + 1) * r1) / 2400);
			System.out.print("Maturity Value: " + a);
			break;
		default:
			System.out.print("Invalid choice");
		}

	}

}
