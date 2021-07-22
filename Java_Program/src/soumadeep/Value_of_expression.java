//Q.. WAP accept the value of x,y,z & display the value of the expression x^3+x^2y^4+z^(3/2)
package soumadeep;

import java.util.Scanner;

public class Value_of_expression {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter value of x: ");
        int x = sc.nextInt();
        System.out.print("Enter value of y: ");
        int y = sc.nextInt();
        System.out.print("Enter value of z: ");
        int z = sc.nextInt();

        double ex = Math.pow(x, 3) + (Math.pow(x, 2) * Math.pow(y, 4)) + Math.pow(z, 1.5);
        System.out.println("Value of expression: " + ex);

    }
}