package soumadeep;

public class SumOfAllPrime {

	public static void main(String[] args) {
		int s = 0, c = 0;
		for (int i = 1; i <= 100; i++) {
			c = 0;
			for (int j = 1; j <= i; j++) {
				if (i % j == 0)
					c++;
			}
			if (c == 2)
				s += i;
		}
		System.out.print("Sum: " + s);

	}

}
