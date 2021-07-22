package soumadeep;

import java.util.Scanner;

public class Year2012_Q8 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("1. Fibonacci Series. \n2. Sum Of DIGITS \nEnter choice: ");
		int n = sc.nextInt();
		switch (n) {
		case 1:
			int a = 0, b = 1, c;
			System.out.print(a + ", " + b + ", ");
			for (int i = 3; i <= 10; i++) {
				c = a + b;
				a = b;
				b = c;
				System.out.print(c + ", ");

			}
			break;

		case 2:
			System.out.print("Enter number: ");
			long num = sc.nextLong();
			int s = 0, d = 0;
			while (num > 0) {
				d = (int) num % 10;
				s += d;
				num /= 10;
			}
			System.out.print("Sum: " + s);
			break;
		default:
			System.out.print("Invaild choice");
		}

	}

}
