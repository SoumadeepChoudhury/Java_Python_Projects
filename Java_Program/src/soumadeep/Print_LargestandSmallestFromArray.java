package soumadeep;

import java.util.Scanner;

public class Print_LargestandSmallestFromArray {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int arr[] = new int[10];
		for (int i = 0; i < 10; i++) {
			System.out.print("Enter value: ");
			arr[i] = sc.nextInt();
		}
		int l = arr[0];
		int s = arr[0];
		for (int i = 1; i < 10; i++) {
			if (arr[i] > l)
				l = arr[i];
			else if (arr[i] < s)
				s = arr[i];
		}

		System.out.print("Largest: " + l + "\nSmallest: " + s);
	}

}
