package soumadeep;

import java.util.Scanner;

// S=x!/10 + (x+2)!/15 + (x+4)!/20 .... (x+n)!/m
public class Series2 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter no. of terms: ");
		int n = sc.nextInt();
		System.out.print("Enter value of x: ");
		int x = sc.nextInt();

		int m = 10;
		double f = 1.0, s = 0;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= x; j++)
				f *= j;
			s += f / m;
			f = 1;
			x += 2;
			m += 5;
		}
		System.out.println("Sum: " + s);
	}

}
