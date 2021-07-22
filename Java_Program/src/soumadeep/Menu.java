package soumadeep;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Menu {
	static double P, r, A;
	static int n;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		System.out.println("1. Term Deposit");
		System.out.println("2. Recurring Deposit");
		System.out.print("Enter Choice (1/2): ");
		int t = Integer.parseInt(br.readLine());
		switch (t) {
		case 1:
			System.out.print("Enter Principal: ");
			P = Double.parseDouble(br.readLine());
			System.out.print("Enter Rate of Interest: ");
			r = Double.parseDouble(br.readLine());
			System.out.print("Enter Time period: ");
			n = Integer.parseInt(br.readLine());
			A = P * Math.pow((1 + r / 100), n);
			System.out.println("Maturity value: " + A);
			break;
		case 2:
			System.out.println("Enter Monthly Installment : ");
			P = Double.parseDouble(br.readLine());
			System.out.println("Enter Rate of Interest: ");
			r = Double.parseDouble(br.readLine());
			System.out.println("Enter time period in months: ");
			n = Integer.parseInt(br.readLine());
			A = (P * n) + ((P * n * (n + 1) * r) / 2400);
			System.out.println("Maturity Amount " + A);
			break;
		default:
			System.out.println("Invalid Choice");
		}

	}

}
