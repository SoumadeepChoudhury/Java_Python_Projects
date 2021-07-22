package soumadeep;

import java.util.Scanner;

public class Year2006_Q8 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		String n[] = new String[5];
		double m[] = new double[5];
		for (int i = 0; i < 5; i++) {
			System.out.print("Enter name: ");
			n[i] = sc.next();
			System.out.print("Enter marks: ");
			m[i] = sc.nextDouble();
		}
		double sum = 0, h = m[0];
		String name = "";

		for (int i = 0; i < m.length; i++) {
			System.out.println(n[i] + " " + m[i]);
			if (h < m[i]) {
				h = m[i];
				name = n[i];
			}
			sum += m[i];
		}
		sum /= 50;
		System.out.println("Average: " + sum);
		System.out.println("Highest score is " + h + " by " + name);

	}

}
