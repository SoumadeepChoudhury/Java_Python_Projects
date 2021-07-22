package soumadeep;

import java.util.Scanner;

public class Anagram {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter a String: ");
        String s = sc.next();
        System.out.print("Enter another String: ");
        String s1 = sc.next();
        s = s.toUpperCase();
        s1 = s1.toUpperCase();
        if (s.length() == s1.length()) {
            int f1 = 0, f2 = 0;
            for (int i = 65; i <= 90; i++) {
                f1 = f2 = 0;
                for (int j = 0; j < s.length(); j++)
                    if (s.charAt(j) == (char) i)
                        f1++;
                for (int j = 0; j < s1.length(); j++)
                    if (s1.charAt(j) == (char) i)
                        f2++;

                if (f1 != f2) {
                    f2 = -1;
                    break;
                }
            }
            if (f2 >= 0)
                System.out.println("Anagram");
            if (f2 < 0)
                System.out.println("Not Anagram");
        } else
            System.out.println("Not Anagram");
    }
}