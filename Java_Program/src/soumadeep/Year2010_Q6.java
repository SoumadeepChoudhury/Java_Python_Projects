package soumadeep;

import java.util.Scanner;

public class Year2010_Q6 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter name: ");
		String n = sc.next();
		System.out.print("Enter ticket amount: ");
		double a = sc.nextDouble();
		double d = 0.0;
		if (a > 70000)
			d = 18.0 / 100 * a;
		else if (a > 55000 && a <= 70000)
			d = 16.0 / 100 * a;
		else if (a > 35000 && a <= 55000)
			d = 12.0 / 100 * a;
		else if (a > 25000 && a <= 35000)
			d = 10.0 / 100 * a;
		else
			d = 2.0 / 100 * a;

		System.out.println("Sl. No. \t Name \t Ticket charges \t Discount \t Net amount");
		System.out.print("1. \t\t " + n + "\t\t" + a + "\t\t" + d + "\t\t" + (a - d));

	}

}
