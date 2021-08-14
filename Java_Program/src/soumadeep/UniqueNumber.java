package soumadeep;

import java.util.Scanner;

public class UniqueNumber {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter number: ");
		int n = sc.nextInt();
		String s = Integer.toString(n);
		int d = 0, f = 0;
		while (n > 0) {
			d = n % 10;
			f = 0;
			for (int i = 0; i < s.length(); i++)
				if (d == Integer.parseInt("" + s.charAt(i)))
					f++;
			n = n / 10;
			if (f > 1) {
				System.out.print("Not Unique number");
				break;
			}
		}
		if (f == 1)
			System.out.print("Unique Number");
	}

}
