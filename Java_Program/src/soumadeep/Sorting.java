package soumadeep;

public class Sorting {

	public static void main(String[] args) {
		int marks[] = { 67, 76, 55, 89, 78 };

		// Bubble Sort

		for (int i = 0; i < marks.length - 1; i++) {
			for (int j = 0; j < marks.length - 1; j++) {
				if (marks[j] > marks[j + 1]) {
					int t = marks[j];
					marks[j] = marks[j + 1];
					marks[j + 1] = t;
				}
			}
		}
		System.out.print("Bubble Sort: ");
		for (int i = 0; i < marks.length; i++) {
			System.out.print(marks[i] + " ");
		}

		// Selection Sort

		for (int i = 0; i < marks.length - 1; i++) {
			int p = i;
			for (int j = i + 1; j < marks.length; j++) {
				if (marks[j] < marks[p]) {
					p = j;
				}
			}

			int t = marks[p];
			marks[p] = marks[i];
			marks[i] = t;
		}
		System.out.print("\nSelection Sort: ");
		for (int i = 0; i < marks.length; i++) {
			System.out.print(marks[i] + " ");
		}
	}

}
