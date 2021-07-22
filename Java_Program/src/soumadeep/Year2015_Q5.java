package soumadeep;

import java.util.Scanner;

public class Year2015_Q5 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter 1/2 : ");
		int ch = sc.nextInt();
		switch (ch) {
		case 1:
			for (int i = 1; i <= 5; i++) {
				for (int j = 1; j <= i; j++) {
					if (j % 2 == 0)
						System.out.print("# ");
					else
						System.out.print("* ");
				}
				System.out.println();
			}
			break;
		case 2:
			for (int i = 1; i <= 5; i++) {
				for (int j = 5; j >= i; j--)
					System.out.print(j + " ");
				System.out.println();
			}
			break;
		default:
			System.out.print("Invalid Choice");
		}

	}

}
