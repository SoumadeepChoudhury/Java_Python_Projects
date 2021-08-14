// # # WAP to print 0,5,10,15,20....till enter -1
package soumadeep;

import java.util.Scanner;

public class Print_Series {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        String value = "";
        int user_Input = 0;
        while (user_Input != -1) {
            System.out.print("Enter value");
            user_Input = sc.nextInt();
            if (user_Input % 5 == 0) {
                value += Integer.toString(user_Input) + " ";
            }
        }
        int x = 0;
        for (int i = 0; i < value.length(); i++) {
            if (value.charAt(i) == 32) {
                System.out.print(value.substring(x, i) + ", ");
                x = i + 1;
            }
        }
    }
}