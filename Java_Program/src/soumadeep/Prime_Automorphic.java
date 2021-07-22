package soumadeep;

import java.util.Scanner;

public class Prime_Automorphic {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		System.out.print("Enter no. :");
		int num = sc.nextInt();

		System.out.print("Enter choice where: \n1. To check if Prime number.\n2. To check if Automorphic Number. ");
		int n = sc.nextInt();
		int n1 = num;
		switch (n) {
		case 1:
			int c = 0;
			for (int i = 1; i <= num; i++)
				if (num % i == 0)
					c++;
			if (c == 2)
				System.out.print("Prime Number");
			else
				System.out.print("Not Prime Number.");
			break;
		case 2:
			int count = 0;
			int sq = (int) Math.pow(num, 2);
			while (num > 0) {
				num /= 10;
				count++;
			}
			int v = (int) Math.pow(10, count);
			sq %= v;
			if (n1 == sq)
				System.out.print("Automorphic number.");
			else
				System.out.print("Not Automorphic Number.");
			break;
		default:
			System.out.print("Invalid choice");
		}

	}

}
