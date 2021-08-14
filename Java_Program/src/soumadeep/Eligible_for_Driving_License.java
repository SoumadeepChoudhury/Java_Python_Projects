// Write a program that takes the name and age of the user as input and displays a message whether the user is eligible to apply for a driving license or not. (the eligible age is 18 years).

package soumadeep;

import java.util.Scanner;

public class Eligible_for_Driving_License {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter name: ");
        String name = sc.next();
        System.out.print("Enter age: ");
        int age = sc.nextInt();

        if (age >= 18)
            System.out.println("Dear " + name + " You are Eligible for Driving license.");
        else
            System.out.println("Dear " + name + " You aren't Eligible for Driving license");
    }
}