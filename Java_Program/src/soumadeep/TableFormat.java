// Write a function to print the table of a given number. The number has to be
// entered by the user.
package soumadeep;

import java.util.Scanner;

public class TableFormat {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter number: ");
        int number = sc.nextInt();
        for (int i = 1; i <= 10; i++) {
            System.out.println(number + " X " + i + " = " + (number * i));
        }
    }

}