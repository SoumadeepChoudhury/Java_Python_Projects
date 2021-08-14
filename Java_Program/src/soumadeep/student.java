package soumadeep;

import java.util.Scanner;

public class student {
	Scanner sc = new Scanner(System.in);
	String name;
	int age;
	double m1, m2, m3, maximum, average;

	student(String name, int age, double m1, double m2, double m3) {
		this.name = name;
		this.age = age;
		this.m1 = m1;
		this.m2 = m2;
		this.m3 = m3;
		maximum = average = 0;
	}

	void details() {
		System.out.print("enter name: ");
		name = sc.next();
		System.out.print("Enter age: ");
		age = sc.nextInt();
		System.out.print("Enter marks in three subjects: ");
		m1 = sc.nextDouble();
		m2 = sc.nextDouble();
		m3 = sc.nextDouble();
	}

	void average() {
		maximum = Math.max(m1, Math.max(m2, m3));
		average = (m1 + m2 + m3) / 3;
	}

	void display() {
		System.out.println("Name: " + name);
		System.out.println("Age: " + age);
		System.out.println("Marks in Three subjects: " + m1 + ", " + m2 + ", " + m3);
		System.out.println("maximum: " + maximum);
		System.out.print("Average: " + average);
	}

	public static void main(String[] args) {
		student ob = new student("sjdf", 16, 88, 99, 74);
		ob.details();
		ob.average();
		ob.display();

	}

}
