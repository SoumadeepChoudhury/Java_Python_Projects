package soumadeep;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// s=1/(1+2) + 1/(1+2+3) + 1/(1+2+3....n)
public class series1 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		System.out.print("Enter n: ");
		int n = Integer.parseInt(br.readLine());
		int t = 1;
		double s = 0;
		for (int i = 2; i <= n; i++) {
			t += i;
			s += 1.0 / t;
		}
		System.out.print(s);

	}

}
