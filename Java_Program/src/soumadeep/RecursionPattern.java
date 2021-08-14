package soumadeep;

public class RecursionPattern {

	public static void main(String[] args) {
		printstar("*", 5);

	}

	/*
	 * To Print
	 * 
	 ** 
	 ***
	 **** 
	 *****
	 */
	static void printstar(String s, int a) {
		if (a == 0)
			return;
		System.out.println(s);
		printstar(s + "*", --a);
	}

}
