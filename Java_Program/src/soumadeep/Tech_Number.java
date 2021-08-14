// WAP find tech numbers through a Java program. A number is called a tech number if the given number has an even number of digits and the number can be divided exactly into two parts from the middle. After equally dividing the number, sum up the numbers and find the square of the sum. If we get the number itself as square, the given number is a tech number, else, not a tech number

package soumadeep;

import java.util.Scanner;

public class Tech_Number {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter a number to check: ");
        int number = sc.nextInt();
        int num = number;
        int count_Digits = 0;
        while (number > 0) {
            count_Digits++;
            number /= 10;
        }
        if (count_Digits % 2 == 0) {
            int part1 = num % ((int) Math.pow(10, (count_Digits / 2)));
            int part2 = num / ((int) Math.pow(10, (count_Digits / 2)));
            int sum = (int) Math.pow((part1 + part2), 2);
            if (sum == num)
                System.out.println("Tech Number");
            else
                System.out.println("Not Tech number");
        }
    }
}