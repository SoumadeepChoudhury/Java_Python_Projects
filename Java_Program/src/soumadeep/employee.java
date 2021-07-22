package soumadeep;

import java.util.Scanner;

public class employee {
	static double basic;
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter basic pay: ");
		basic = sc.nextDouble();
		double da = 25.0 / 100 * basic;
		double hra = 15.0 / 100 * basic;
		double pf = 8.33 / 100 * basic;
		double net = basic + da + hra;
		double gross = net - pf;
		System.out.print("Gross: " + gross);

	}

}
