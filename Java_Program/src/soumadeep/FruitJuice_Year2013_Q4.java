package soumadeep;

import java.util.Scanner;

public class FruitJuice_Year2013_Q4 {
	static Scanner sc = new Scanner(System.in);

	int product_code, pack_size, product_price;
	String flavour, pack_type;

	FruitJuice_Year2013_Q4() {
		product_code = pack_size = product_price = 0;
		flavour = pack_type = "";
	}

	void input() {
		System.out.print("Enter product code: ");
		product_code = sc.nextInt();
		System.out.print("Enter pack size: ");
		pack_size = sc.nextInt();
		System.out.print("Enter flavour: ");
		flavour = sc.next();
		System.out.print("Enter pack type: ");
		pack_type = sc.next();
		System.out.print("Enter product price: ");
		product_price = sc.nextInt();
	}

	void discount() {
		product_price -= 10;
	}

	void display() {
		System.out.print("Product code: " + product_code + "\nFlavour: " + flavour + "\nPack Type: " + pack_type
				+ "\nPack Size: " + pack_size + "\nProduct Price: " + product_price);

	}

	public static void main(String[] args) {
		FruitJuice_Year2013_Q4 ob = new FruitJuice_Year2013_Q4();
		ob.input();
		ob.discount();
		ob.display();
	}

}
