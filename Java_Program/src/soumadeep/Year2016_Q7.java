package soumadeep;

public class Year2016_Q7 {
	void SumSeries(int n, double x) {
		double s = 0;
		int k = 2;
		for (int i = 1; i <= n; i++) {
			s += (x / i * Math.pow(-1, k));
			k += 1;
		}
		System.out.print("Sum: " + s);
	}

	void SumSeries() {
		int s = 0, t = 1;
		for (int i = 1; i <= 20; i++) {
			t *= i;
			s += t;
		}
		System.out.print("Sum: " + s);
	}

	public static void main(String[] args) {
		Year2016_Q7 ob = new Year2016_Q7();
		ob.SumSeries(2, 2);
		ob.SumSeries();
	}

}
