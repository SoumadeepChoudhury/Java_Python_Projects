package soumadeep;

import java.util.Scanner;

public class TestPaper2 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int a[] = { 5, 7, 9, 11, 15, 20, 30, 45, 89, 97 };
		System.out.print("Enter searching elememt: ");
		int x = sc.nextInt();
		int start = 0;
		int end = a.length - 1;
		int p = -1;
		while (start <= end) {
			int mid = (start + end) / 2;
			if (a[mid] == x) {
				p = mid;
				break;
			}
			if (x < a[mid])
				end = mid - 1;
			else
				start = mid + 1;
		}
		if (p == -1)
			System.out.print("Not found");
		else
			System.out.print("Found at: " + (p + 1));
	}

}
