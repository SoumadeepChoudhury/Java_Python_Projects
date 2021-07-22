package soumadeep;

import java.util.Scanner;

public class Y2009_Q4 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter name: ");
		String n = sc.next();
		System.out.print("Enter address: ");
		String a = sc.next();
		System.out.print("Enter amount of purchase: ");
		double am = sc.nextDouble();
		System.out.print("Enter L/D: ");
		char c = sc.next().charAt(0);
		double d = 0.0;

		if (am <= 25000) {
			if (c == 'L')
				d = 0.0;
			else if (c == 'D')
				d = 5.0 / 100 * am;
		} else if (am > 25000 && am <= 57000) {
			if (c == 'L')
				d = 5.0 / 100 * am;
			else if (c == 'D')
				d = 7.6 / 100 * am;
		} else if (am > 57000 && am <= 100000) {
			if (c == 'L')
				d = 7.5 / 100 * am;
			else if (c == 'D')
				d = 10.0 / 100 * am;
		} else if (c == 'L')
			d = 10.0 / 100 * am;
		else if (c == 'D')
			d = 15.0 / 100 * am;

		System.out.println("Name: " + n);
		System.out.println("Address: " + a);
		System.out.println("Amount to pay: " + (am - d));
	}

}
