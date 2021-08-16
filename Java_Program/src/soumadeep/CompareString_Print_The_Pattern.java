// WAP that takes two strings as input and displays the smaller string in single line and the larger string as per this format...
/*
1st letter                  last letter
    2nd letter             2nd last lettter
        3rd letter      3rd last letter
                    :
*/

package soumadeep;

import java.util.Scanner;

public class CompareString_Print_The_Pattern {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter 1st text: ");
        String user_Input1 = sc.next();
        System.out.print("Enter 2st text: ");
        String user_Input2 = sc.next();
        String large = "";
        if (user_Input1.compareTo(user_Input2) > 0) {
            System.out.println("Smaller String: " + user_Input2);
            large = user_Input1;

        } else if (user_Input1.compareTo(user_Input2) < 0) {
            System.out.println("Smaller String: " + user_Input1);
            large = user_Input1;
        } else
            System.out.println("Both are same.");

        int k = 2;
        for (int i = 0; i < Math.round(large.length() / 2); i++) {
            for (int j = 0; j < i; j++)
                System.out.print(" ");
            System.out.print(large.charAt(i));
            for (int j = 0; j < large.length() - k; j++)
                System.out.print(" ");
            k += 2;
            System.out.println(large.charAt(large.length() - i - 1));
        }
    }
}