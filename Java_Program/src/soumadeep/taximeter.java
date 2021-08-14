package soumadeep;

import java.util.Scanner;

public class taximeter {
	static Scanner sc = new Scanner(System.in);
	int taxino, km, b;
	String name;

	taximeter() {
		taxino = km = b = 0;
		name = " ";
	}

	void input() {
		System.out.print("Enter taxino. : ");
		taxino = sc.nextInt();
		System.out.print("Enter name: ");
		name = sc.next();
		System.out.print("Enter KM : ");
		km = sc.nextInt();
	}

	void calculate() {
		if (km <= 1)
			b = 25 * km;
		else if (km > 1 && km <= 6)
			b = 10 * km;
		else if (km > 6 && km <= 12)
			b = 15 * km;
		else if (km > 12 && km <= 18)
			b = 20 * km;
		else
			b = 25 * km;
	}

	void display() {
		System.out.println("Taxi No. \t Name \t Kilometers travelled \t Bill Amount");
		System.out.print(taxino + "\t\t" + name + "\t\t" + km + "\t\t\t" + b);
	}

	public static void main(String[] args) {
		taximeter ob = new taximeter();
		ob.input();
		ob.calculate();
		ob.display();

	}

}
