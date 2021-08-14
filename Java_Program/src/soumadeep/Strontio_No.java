package soumadeep;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Strontio_No {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		System.out.print("Enter 4 digit no: ");
		int n = Integer.parseInt(br.readLine());
		n *= 2;
		String s = Integer.toString(n);
		char c[] = s.toCharArray();
		if (c[1] == c[2])
			System.out.print("The number you entered is Strontio number");
		else
			System.out.print("The number you entered is not Strontio number");
	}

}
