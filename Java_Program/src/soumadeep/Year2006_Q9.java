package soumadeep;

import java.util.Scanner;

public class Year2006_Q9 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int n[] = new int[15];
		int x = 0;
		for (int i = 0; i < n.length; i++) {
			System.out.print("Enter no: ");
			n[i] = sc.nextInt();
			if (n[i] == 0) {
				x++;
				System.out.print("You have entered ZERO");
				break;
			}
		}
		if (x == 0) {
			for (int i = 0; i < n.length - 1; i++) {
				int p = i;
				for (int j = i + 1; j < n.length; j++) {
					if (n[j] < n[p])
						p = j;
				}

				int t = n[p];
				n[p] = n[i];
				n[i] = t;
			}

			for (int i = 0; i < n.length; i++) {
				System.out.println(n[i]);
			}
		}
	}

}
