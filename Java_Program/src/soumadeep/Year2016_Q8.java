package soumadeep;

import java.util.Scanner;

public class Year2016_Q8 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter A number: ");
		int n = sc.nextInt();
		int n1 = n;
		int sum = 0;
		while (n > 0) {
			int d = n % 10;
			sum += d;
			n /= 10;
		}
		if (n1 % sum == 0)
			System.out.print("Niven Number");
		else
			System.out.print("Not Niven Number");

	}

}
