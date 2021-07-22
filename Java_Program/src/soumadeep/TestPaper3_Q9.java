package soumadeep;

import java.util.Scanner;

public class TestPaper3_Q9 {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter String: ");
        String s = sc.next().toLowerCase();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'a' || s.charAt(i) == 'e' || s.charAt(i) == 'i' || s.charAt(i) == 'o'
                    || s.charAt(i) == 'u')
                s = s.replace(s.charAt(i), (char) (s.charAt(i) + 1));
        }
        System.out.println("New String: " + s);
    }
}