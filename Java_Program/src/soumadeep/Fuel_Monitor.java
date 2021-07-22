package soumadeep;

import java.util.Scanner;

public class Fuel_Monitor {
	static Scanner sc = new Scanner(System.in);
	int tankCapacity, efficiency, fuel_in_tank = 0, fuel_to_fill, distance;

	Fuel_Monitor() {
		System.out.print("Enter tank Capacity: ");
		tankCapacity = sc.nextInt();
		System.out.print("Enter efficiency : ");
		efficiency = sc.nextInt();
		System.out.print("Enter fuel present in tank: ");
		fuel_in_tank = sc.nextInt();
	}

	int add_fuel() {
		fuel_to_fill = tankCapacity - fuel_in_tank;
		return fuel_to_fill;
	}

	int drive() {
		distance = 5 * fuel_in_tank;
		return distance;
	}

	public static void main(String[] args) {
		Fuel_Monitor ob = new Fuel_Monitor();
		System.out.println(ob.add_fuel());
		System.out.println(ob.drive());

	}

}
