package soumadeep;

import java.util.Scanner;

public class UserChoice {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int n = 0;
		int s1 = 0, s2 = 0, s3 = 0;
		do {
			System.out.print("Enter value: ");
			int v = sc.nextInt();
			n = v;
			if (v < 0)
				s1 += v;
			else if (v > 0 && v % 2 == 0)
				s2 += v;
			else if (v > 0 && v % 2 != 0)
				s3 += v;
		} while (n != 0);
		System.out.println("Sum of negative numbers: " + s1);
		System.out.println("Sum of positive even numbers: " + s2);
		System.out.print("Sum of positive odd numbers: " + s3);

	}

}
