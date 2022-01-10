// Check for happy number. eg: 32,23,10
package soumadeep;

import java.util.Scanner;

public class Happy_Number {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("enter number: ");
        int user_Inp = sc.nextInt();
        int sum = 0, x = user_Inp;
        while (sum != 1) {
            sum = 0;
            while (x > 0) {
                int d = x % 10;
                sum += d * d;
                x /= 10;
            }
            x = sum;
            if (sum > user_Inp)
                break;
        }
        if (sum == 1)
            System.out.println("Happy Number");
        else {
            System.out.println("Not Happy Number");
        }
    }
}