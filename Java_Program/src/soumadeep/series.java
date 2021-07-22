package soumadeep;

public class series {

	public static void main(String[] args) {		
		double sum = 0, a = 2.0;
		for (int i = 1; i <= 2; i++) {
			sum += i;
			sum += (i + a) / i * (i + a);
			++a;
		}
		System.out.println(sum);

	}

}