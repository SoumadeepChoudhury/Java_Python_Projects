package soumadeep;

import java.util.Scanner;

public class Year2006_Q4 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter n: ");
		int n = sc.nextInt();
		int se = 0, so = 0;
		for (int i = 1; i <= n; i++) {
			if (i % 2 == 0)
				se += i;
			else
				so += i;
		}
		System.out.println("Even's sum: " + se);
		System.out.print("Odds' sum: " + so);
	}

}
