package soumadeep;

import java.util.Scanner;

public class TestPaper3_Q7 {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter String: ");
        String s = sc.nextLine();
        // String new_s="";
        for (int i = 0; i < s.length(); i++) {
            if (Character.isUpperCase(s.charAt(i)) == true)
                System.out.print(Character.toLowerCase(s.charAt(i)));
            else
                System.out.print(Character.toUpperCase(s.charAt(i)));
        }
        System.out.println(); // moving the curser to the next line
    }

}