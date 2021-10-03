// Create a Java program to check if the given number is Neon Number or not. A positive integer whose sum of digits of its square is equal to the number itself is called a neon number.

package soumadeep;

import java.util.Scanner;

public class Neon_Number {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter a number to check: ");
        int user_Input = sc.nextInt();
        int squared = (int) Math.pow(user_Input, 2);
        int sum = 0;
        while (squared > 0) {
            int d = squared % 10;
            sum += d;
            squared /= 100;
        }
        if (sum == user_Input) {
            System.out.println("It is a Neon Number.");
        } else {
            System.out.println("It is not a Neon Number.");
        }
    }
}