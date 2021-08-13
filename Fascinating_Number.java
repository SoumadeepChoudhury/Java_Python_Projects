//WAP to check a given number is fascinating number or not... Multiplying a number by two and three separately, the number obtained by writing the results obtained with the given number will be called a fascinating number. If the result obtained after concatenation contains all digits from 1 to 9, exactly once. Some other fascinating numbers are 192, 219, 273, 327, 1902, 1920, 2019 etc.

package soumadeep;

import java.util.Scanner;

class Fascinating_Number {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Enter Number: ");
        int number = sc.nextInt();
        String final_String = Integer.toString(number) + Integer.toString(number * 2) + Integer.toString(number * 3);
        int count = 0;
        for (int i = '1'; i <= '9'; i++) {
            for (int j = 0; j < final_String.length(); j++) {
                if (final_String.charAt(j) == i) {
                    count++;
                    final_String = final_String.replace(final_String.charAt(j), ' ');
                }
            }
        }
        if (count >= 9)
            System.out.println("Fascinating Number");
        else
            System.out.println("Not a Fascinating number");
    }
}