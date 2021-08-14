// Check if prime..
package soumadeep;

import java.util.Scanner;

public class PractiseProgram2 {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Enter number: ");
        int x = sc.nextInt();
        int c = 0;
        for (int i = 1; i <= x; i++) {
            if (x % i == 0)
                c++;
        }
        if (c == 2)
            System.out.println("Prime");
        else
            System.out.println("Not Prime");
    }
}