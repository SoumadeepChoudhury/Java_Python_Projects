// Write a program that prints minimum and maximum of five numbers entered by the user.
package soumadeep;

import java.util.Scanner;

public class Max_Min {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int arr[] = new int[5];
        int max, min;
        for (int i = 1; i <= 5; i++) {
            System.out.print("Enter number " + i + ": ");
            arr[i - 1] = sc.nextInt();
        }
        max = min = arr[0];
        for (int i = 0; i < 5; i++) {
            if (arr[i] > max)
                max = arr[i];
            else if (arr[i] < min)
                min = arr[i];
        }
        System.out.println("Max: " + max);
        System.out.println("Min: " + min);
    }
}