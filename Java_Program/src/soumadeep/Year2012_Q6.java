package soumadeep;

import java.util.Scanner;

public class Year2012_Q6 {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter sentence: ");
        String s = sc.nextLine().toUpperCase();
        int f = 0;
        for (int i = 0; i < s.length() - 1; i++)
            if (s.charAt(i) == s.charAt(i + 1))
                f++;
        System.out.println(f);
    }
}