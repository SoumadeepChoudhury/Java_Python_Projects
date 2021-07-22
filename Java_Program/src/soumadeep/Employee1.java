package soumadeep;

import java.util.Scanner;

public class Employee1 {
	Scanner sc = new Scanner(System.in);
	int pan;
	String name;
	double taxincome, tax;

	void input() {
		System.out.print("Enter pan Number: ");
		pan = sc.nextInt();
		System.out.print("Enter name: ");
		name = sc.next();
		System.out.print("Enter taxable income: ");
		taxincome = sc.nextDouble();
	}

	void calc() {
		if (taxincome <= 100000)
			tax = 0;
		else if (taxincome > 100000 && taxincome <= 150000)
			tax = 10.0 / 100 * (taxincome - 100000);
		else if (taxincome > 150000 && taxincome <= 250000)
			tax = 5000 + (20.0 / 100 * (taxincome - 150000));
		else
			tax = 25000 + (30.0 / 100 * (taxincome - 250000));
	}

	void display() {
		System.out.println("Name \t PAN \t Income \t Tax");
		System.out.print(name + "\t" + pan + "\t" + taxincome + "\t" + tax);
	}

	public static void main(String[] args) {
		Employee1 ob = new Employee1();
		ob.input();
		ob.calc();
		ob.display();
	}

}
