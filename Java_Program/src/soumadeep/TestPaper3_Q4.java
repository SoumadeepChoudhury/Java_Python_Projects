package soumadeep;

import java.util.Scanner;

public class TestPaper3_Q4 {
	Scanner sc = new Scanner(System.in);
	int bno, phno, days, charge;
	String name;

	void input() {
		System.out.print("Enter Bike Number: ");
		bno = sc.nextInt();
		System.out.print("Enter Phone number: ");
		phno = sc.nextInt();
		System.out.print("Enter Name: ");
		name = sc.next();
		System.out.print("Enter no. of days bike taken on rent: ");
		days = sc.nextInt();
	}

	void compute() {
		if (days <= 5)
			charge = 500 * days;
		else if (days <= 10)
			charge = 2500 + (days - 5) * 400;
		else
			charge = 2500 + 2000 + (days - 10) * 200;
	}

	void display() {
		System.out.println("Bike No. \t Phone no. \t Name \t No. of days \t Charge");
		System.out.print(bno + "\t" + phno + "\t" + name + "\t" + days + "\t" + charge);
	}

	public static void main(String[] args) {
		TestPaper3_Q4 ob = new TestPaper3_Q4();
		ob.input();
		ob.compute();
		ob.display();
	}

}
