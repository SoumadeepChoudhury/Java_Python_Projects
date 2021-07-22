package soumadeep;

import java.util.Scanner;

public class Year2018_Q5 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String args[]) {
		System.out.print("Enter number: ");
		int n = sc.nextInt();
		int p = 1, x = 0;
		for (int i = 1; i < n; i++) {
			p = i * (i + 1);
			if (p == n) {
				System.out.print("Pronic Number");
				x++;
				break;
			}
		}
		if (x == 0)
			System.out.print("Not Pronic Number");
	}
}
