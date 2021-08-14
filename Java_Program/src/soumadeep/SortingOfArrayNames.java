package soumadeep;

import java.util.Scanner;

public class SortingOfArrayNames {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		String n[] = new String[10];

		for (int i = 0; i < 10; i++) {
			System.out.print("Enter name in Capital Letters: ");
			n[i] = sc.next().toUpperCase();
		}

		for (int i = 0; i < n.length - 1; i++) {
			int p = i;
			for (int j = i + 1; j < n.length; j++) {
				if (n[p].compareTo(n[j]) > 0)
					p = j;
			}

			String x = n[p];
			n[p] = n[i];
			n[i] = x;
		}

		for (int i = 0; i < 10; i++) {
			System.out.println(n[i]);
		}

	}

}
