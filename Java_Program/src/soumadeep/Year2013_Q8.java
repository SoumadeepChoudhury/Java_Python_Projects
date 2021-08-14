package soumadeep;

public class Year2013_Q8 {
	double series(double n) {
		double s = 0;
		for (int i = 1; i <= n; i++) {
			s += 1.0 / i;
		}
		return s;
	}

	double series(double a, double n) {
		double sum = 0;
		int x = 1, y = 2;
		for (int i = 1; i <= n; i++) {
			sum += x / Math.pow(a, y);
			x += 3;
			y += 3;
		}
		return sum;
	}

	public static void main(String[] args) {
		Year2013_Q8 ob = new Year2013_Q8();
		System.out.println(ob.series(2.0));
		System.out.print(ob.series(1.0, 2.0));

	}

}
