package soumadeep;

import java.util.Scanner;

public class Year2015_Q9 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("1. Display factors of a number. \n2. Display factorial. \nEnter choice 1/2: ");
		int n = sc.nextInt();
		switch (n) {
		case 1:
			System.out.print("Enter number: ");
			int x = sc.nextInt();
			for (int i = 1; i < x; i++) {
				if (x % i == 0)
					System.out.print(i + ", ");
			}
			break;
		case 2:
			System.out.print("Enter number: ");
			int x1 = sc.nextInt();
			int f = 1;
			for (int i = 1; i <= x1; i++)
				f *= i;
			System.out.print("Factorial: " + f);
			break;
		default:
			System.out.print("Invalid choice");
		}
	}

}
