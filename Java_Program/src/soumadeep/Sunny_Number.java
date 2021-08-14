// WAP to find whether a number input by user is a sunny number or not? A number is called a sunny number if the number next to the given number is a perfect square. In other words, a number N will be a sunny number if N+1 is a perfect square.
package soumadeep;

import java.util.Scanner;

public class Sunny_Number {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter a number: ");
        int number = sc.nextInt();
        number++;
        if (Math.sqrt(number) - (int) Math.sqrt(number) == 0)
            System.out.println("Sunny Number");
        else
            System.out.println("Not a Sunny Number");
    }
}