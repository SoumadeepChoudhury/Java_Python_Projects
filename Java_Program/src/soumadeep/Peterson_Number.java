// WAP check whether a given number is Peterson or not through a Java program.A number is said to be Peterson if the sum of factorials of each digit is equal to the sum of the number itself.
package soumadeep;

import java.util.Scanner;

public class Peterson_Number {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter a number: ");
        int number = sc.nextInt();
        int x = number;
        int sum = 0;
        while (number > 0) {
            int d = number % 10;
            number /= 10;
            int f = 1;
            for (int i = 1; i <= d; i++) {
                f *= i;
            }
            sum += f;
        }
        if (sum == x)
            System.out.println("Peterson Number");
        else
            System.out.println("Not a Peterson Number");
    }
}
