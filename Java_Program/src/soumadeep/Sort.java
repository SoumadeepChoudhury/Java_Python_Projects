package soumadeep;

public class Sort {

	public static void main(String[] args) {
		int v[] = { 5, 3, 8, 4, 9, 2, 1, 12, 98, 16 };
		for (int i = 0; i < v.length - 1; i++) {
			for (int j = 0; j < v.length - 1; j++) {
				if (v[j] > v[j + 1]) {
					int t = v[j];
					v[j] = v[j + 1];
					v[j + 1] = t;
				}
			}
		}
		for (int i = 0; i < v.length; i++) {
			System.out.println(v[i]);
		}

	}

}
