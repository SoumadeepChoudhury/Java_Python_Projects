package soumadeep;

public class Pattern {

	public static void main(String[] args) {		
		System.out.println("***********************");
		for (int i = 0; i < 20; i++) {
			for (int j = 20; j >= i; j--)
				System.out.print(" ");
			System.out.println("*");
		}
		System.out.println("*********************");
	}

}
