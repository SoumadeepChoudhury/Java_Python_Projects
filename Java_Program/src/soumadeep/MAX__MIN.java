// WAP to find max and min of a number of inputs without using array.

package soumadeep;

import java.util.Scanner;

public class MAX__MIN {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        float max = 0, min = 0;
        boolean first = true;
        while (true) {
            System.out.print("Enter number: ");
            float userInp = sc.nextFloat();
            if (userInp > max) {
                max = userInp;
                if (first) {
                    min = userInp;
                    first = false;
                }
            } else if (userInp < min)
                min = userInp;
            System.out.print("Do You wanna continue ?[y/n] ");
            String ch = sc.next().toLowerCase();
            if (ch.equals("n"))
                break;
        }
        System.out.println("Max: " + max);
        System.out.println("Min: " + min);
    }
}
