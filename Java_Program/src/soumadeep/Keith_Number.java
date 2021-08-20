//A positive n digit number X is called a Keith number (or repfigit number) if it is arranged in a special number sequence generated using its digits. The special sequence has first n terms as digits of x and other terms are recursively evaluated as the sum of previous n terms. For example, 197, 19, 742, 1537, etc. The program stops if the value computed is greater than the input number.

package soumadeep;

import java.util.Scanner;

class Keith_Number {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter a number to check for Keith or not: ");
        int number = sc.nextInt();
        int sum = 0;
        int num = number;
        int arr[] = new int[Integer.toString(number).length()];
        int i = -1;
        while (number != 0) {
            i++;
            int d = number % 10;
            arr[arr.length - 1 - i] = d;
            number /= 10;
        }
        while (sum != num) {
            sum = 0;
            for (int j = 0; j < arr.length; j++)
                sum += arr[j];
            for (int j = 0; j < arr.length; j++)
                if (j + 1 == arr.length)
                    arr[j] = sum;
                else
                    arr[j] = arr[j + 1];
            if (sum == num)
                System.out.println("Keith Number");
            else if (sum > num) {
                System.out.println("Not a Keith Number");
                break;
            }
        }
    }
}