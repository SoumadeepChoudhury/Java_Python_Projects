package soumadeep;

import java.util.Scanner;

public class Year2012_Q4 {
	Scanner sc = new Scanner(System.in);
	int acc_num;
	String title, author;

	void input() {
		System.out.print("Enter accession number: ");
		acc_num = sc.nextInt();
		System.out.print("Enter title: ");
		title = sc.next();
		System.out.print("Enter name of author: ");
		author = sc.next();
	}

	void compute() {
		System.out.print("Enter number of days late: ");
		int days = sc.nextInt();
		int fn = days * 2;
		System.out.println("Fine: Rs. " + fn);
	}

	void display() {
		System.out.println("Accession Number. \t Title \t Author");
		System.out.print(acc_num + "\t\t    " + title + "\t" + author);
	}

	public static void main(String[] args) {
		Year2012_Q4 ob = new Year2012_Q4();
		ob.input();
		ob.compute();
		ob.display();

	}

}
