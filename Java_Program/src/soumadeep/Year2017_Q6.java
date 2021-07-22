package soumadeep;

import java.util.Scanner;

public class Year2017_Q6 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("1. Sum of Series \n2. Display Series \nEnter choice: ");
		int ch = sc.nextInt();
		switch (ch) {
		case 1:
			int x = 2, k = 2;
			double s = 0;
			for (int i = 1; i <= 20; i++) {
				s += Math.pow(x, i) * Math.pow(-1, k);
				k++;
			}
			System.out.print("Sum: " + s);
			break;
		case 2:
			int t = 0, d = 1;
			for (int i = 1; i <= 5; i++) {
				t += d;
				d = d * 10;
				System.out.print(t + " ");
			}
			break;
		default:
			System.out.print("Invaild choice");
		}

	}

}
