// WAP a program to find GCD and LCM of two numbers.
package soumadeep;

import java.util.Scanner;

class GCD_LCM {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter first number ");
        int n1 = sc.nextInt();
        System.out.print("Enter second number ");
        int n2 = sc.nextInt();
        int b = n1;
        int gcd = 0, lcd = 0;
        if (n1 > n2)
            b = n2;
        for (int i = 1; i <= b; i++) {
            if (n1 % i == 0 && n2 % i == 0)
                gcd = i;
        }
        lcd = (n1 * n2) / gcd;
        System.out.println("GCD: " + gcd);
        System.out.println("LCM: " + lcd);
    }
}