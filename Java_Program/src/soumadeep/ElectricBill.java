package soumadeep;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ElectricBill {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	String n;
	int units;
	double bill;

	void accept() throws IOException {
		System.out.print("Enter name: ");
		n = br.readLine();
		System.out.print("Enter Number of units consumed: ");
		units = Integer.parseInt(br.readLine());
	}

	void calculate() {
		if (units <= 100)
			bill = 2 * units;
		else if (units > 100 && units <= 300)
			bill = 200 + 3 * (units - 100);
		else if (units > 300) {
			bill = 200 + 600 + 5 * (units - 300);
			bill += 2.5 / 100 * bill;
		}
	}

	void print() {
		System.out.println("Name of Customer: " + n);
		System.out.println("Number of units: " + units);
		System.out.println("Bill amount: " + bill);
	}

	public static void main(String[] args) throws IOException {
		ElectricBill ob = new ElectricBill();
		ob.accept();
		ob.calculate();
		ob.print();
	}

}
