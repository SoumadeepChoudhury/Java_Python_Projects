package soumadeep;

import java.util.Scanner;

public class TestPaper2_Q7 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter choice: \n1. Triangle\n2. Inverted Triangle");
		int ch = sc.nextInt();
		switch (ch) {
		case 1:
			System.out.print("Enter no of terms: ");
			int x = sc.nextInt();
			for (int i = 1; i <= x; i++) {
				for (int j = 1; j <= i; j++)
					System.out.print(i + " ");
				System.out.println();
			}
			break;
		case 2:
			System.out.print("Enter no of terms: ");
			x = sc.nextInt();
			for (int i = x; i >= 1; i--) {
				for (int j = 1; j <= i; j++)
					System.out.print(i + " ");
				System.out.println();
			}
			break;
		default:
			System.out.print("Invalid choice");
		}
	}
}
