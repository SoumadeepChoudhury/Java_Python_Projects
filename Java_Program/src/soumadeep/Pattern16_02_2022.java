/*

@
#@
@#@
#@#@
@#@#@

*/
package soumadeep;

import java.util.Scanner;

public class Pattern16_02_2022 {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter Max Row: ");
        int max_row = sc.nextInt();
        for (int i = 0; i < max_row; i++) {
            for (int j = 0; j <= i; j++) {
                if (i % 2 == 0 && j % 2 != 0)
                    System.out.print("#");
                else if (i % 2 != 0 && j % 2 == 0)
                    System.out.print("#");
                else
                    System.out.print("@");
            }
            System.out.println();
        }
    }
}