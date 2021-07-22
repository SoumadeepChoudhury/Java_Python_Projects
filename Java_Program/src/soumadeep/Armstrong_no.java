package soumadeep;

import java.util.Scanner;

public class Armstrong_no {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {		
		System.out.print("Enter n: ");
		int n = sc.nextInt();
		int a[] = new int[n];
		for (int i = 0; i < a.length; i++) // creating input in array
		{
			System.out.print("Enter numbers: ");
			a[i] = sc.nextInt();
		}
		for (int i = 0; i < a.length; i++) {
			int d = 0, k = 0;
			int x = a[i];
			while (a[i] > 0) {
				k = a[i] % 10;
				d += (k * k * k);
				a[i] = a[i] / 10;
			}
			if (x == d)
				System.out.println(x);
		}
	}

}
