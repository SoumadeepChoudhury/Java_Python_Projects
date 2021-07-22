package soumadeep;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class strings {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		System.out.print("Enter string: ");
		String s = br.readLine();
		String n = s.toUpperCase();
		int tc = s.length();
		int v = 0;
		for (int i = 0; i < tc; i++) {
			if (n.charAt(i) == 'A' || n.charAt(i) == 'E' || n.charAt(i) == 'I' || n.charAt(i) == 'O'
					|| n.charAt(i) == 'U')
				v++;
		}
		n = "";
		char c[] = s.toCharArray();
		char cr[] = new char[s.length()];
		for (int i = 0; i < c.length; i++) {
			cr[i] = c[s.length() - 1 - i];
			n += cr[i];
		}
		System.out.println("Total no. of characters: " + tc);
		System.out.println("Total no. of vowels: " + v);
		System.out.print("Reverse String: " + n);
	}

}
