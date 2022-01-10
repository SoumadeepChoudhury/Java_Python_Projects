// Amicable number is such a number where user will take 2 inputs as int. And if the sum of the factors of the first number is equal to the second number and vice versa...then it's an Amicable number...E.g..220 and 284 are amicable number
package soumadeep;

import java.util.Scanner;

public class Amicable_Number {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter the values to check: ");
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int sum1 = 0, sum2 = 0;
        for (int i = 1; i < num1; i++) {
            if (num1 % i == 0)
                sum1 += i;
        }
        for (int i = 1; i < num2; i++) {
            if (num2 % i == 0)
                sum2 += i;
        }
        if (sum1 == num2 && sum2 == num1) {
            System.out.println("Amicable number");
        } else {
            System.out.println("Not Amicable number");
        }
    }
}