package soumadeep;

import java.util.Scanner;

public class cal {
	static Scanner sc = new Scanner(System.in);

	void area(double r) {
		System.out.print(3.14 * r * r);
	}

	void area(float a) {
		System.out.print(a * a);
	}

	void area(double l, double b) {
		System.out.print(l * b);
	}

	public static void main(String[] args) {
		System.out.println("1. Area of Circle");
		System.out.println("2. Area of Square");
		System.out.println("3. Area of Rectangle");
		System.out.println("Enter choice: ");
		int n = sc.nextInt();
		cal c = new cal();
		switch (n) {
			case 1:
				System.out.println("Enter radius: ");
				double r = sc.nextDouble();
				c.area(r);
				break;
			case 2:
				System.out.println("Enter side: ");
				float a = sc.nextFloat();
				c.area(a);
				break;
			case 3:
				System.out.println("Enter length & breadth: ");
				double l = sc.nextDouble();
				double b = sc.nextDouble();
				c.area(l, b);
				break;
			default:
				System.out.println("Invalid choice");
		}

	}

}
