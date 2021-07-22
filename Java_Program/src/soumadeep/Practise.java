package soumadeep;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Practise {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		int arr[] = new int[5];
		System.out.println(arr); // garbage value

		System.out.println("Enter number: ");
		String n = br.readLine();
		n = n.trim();
		int s = 0, p = 1;
		char ch[] = n.toCharArray();
		for (int i = 0; i < ch.length; i++) {
			s += Integer.parseInt("" + ch[i]);
			p *= Integer.parseInt("" + ch[i]);
		}
		if (s == p)
			System.out.println("Year2017_Q5 no.");
	}

}
