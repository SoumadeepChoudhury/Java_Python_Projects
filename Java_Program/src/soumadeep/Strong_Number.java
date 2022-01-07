//Strong number is a special number whose sum of the factorial of digits is equal to the original number. For Example: 145 is strong number
package soumadeep;

import java.util.Scanner;

public class Strong_Number {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter one number to check;");
        int userInp = sc.nextInt();
        int x = userInp, sum1 = 0;
        while (userInp > 0) {
            int d = userInp % 10;
            int f = 1;
            for (int i = 1; i <= d; i++) {
                f *= i;
            }
            sum1 += f;
            userInp /= 10;
        }
        if (x == sum1)
            System.out.println("Strong Number");
        else
            System.out.println("Not Strong Number");
    }

}
