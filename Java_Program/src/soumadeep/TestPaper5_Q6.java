package soumadeep;

import java.util.Scanner;

public class TestPaper5_Q6 {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter a sentence: ");
        String s = sc.nextLine();
        s += " ";
        int p = 0, l = 0;
        String s1 = "";
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 32) {
                s1 = s.substring(p, i);
                p = i + 1;
                if (l < s1.length())
                    l = s1.length();
            }
        }
        System.out.println("No of Characters: " + l);
    }
}