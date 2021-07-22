package soumadeep;

import java.util.Scanner;

public class Year2016_Q5 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter 1/2: ");
		int ch = sc.nextInt();
		switch (ch) {
		case 1:
			int a = 1;
			for (int i = 1; i <= 5; i++) {
				for (int j = 1; j <= i; j++) {
					System.out.print(a++ + " ");
				}
				System.out.println();
			}
			break;
		case 2:
			String s = "ICSE";
			for (int i = 1; i <= 4; i++) {
				for (int j = 0; j < i; j++)
					System.out.print(s.charAt(j) + " ");
				System.out.println();
			}
			break;
		default:
			System.out.print("Invalid Choice");
		}

	}

}
