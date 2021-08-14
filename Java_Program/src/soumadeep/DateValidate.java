// Programm to validate date.

package soumadeep;

import java.util.Scanner;

public class DateValidate {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter date in dd/mm/yyyy: ");
        String s = sc.nextLine();

        if (s.substring(0, 2).length() != 2 || s.substring(3, 5).length() != 2 || s.substring(6).length() != 4) {
            System.out.println("Enter date properly.");
            System.exit(0);
        }
        int day = Integer.parseInt(s.substring(0, 2));
        int month = Integer.parseInt(s.substring(3, 5));
        int year = Integer.parseInt(s.substring(6));

        if (year % 4 != 0) {
            if (month == 2 && day <= 28)
                System.out.println("Date Validation Successful..:)");
            else if ((month < 8 && month % 2 != 0 && month != 2) && day < 32)
                System.out.println("Date Validation successfull...:)");
            else if ((month > 7 && month % 2 == 0 && month != 2) && day < 32)
                System.out.println("Date Validation Successful...:)");
            else if (day <= 30 && month != 2)
                System.out.println("Date Validation Successful...:)");
            else
                System.out.println("Date Validation Not successful...:(");
        } else {
            if (month == 2 && day <= 29)
                System.out.println("Date Validation Successful..:)");
            else if ((month < 8 && month % 2 != 0 && month != 2) && day < 32)
                System.out.println("Date Validation successfull...:)");
            else if ((month > 7 && month % 2 == 0 && month != 2) && day < 32)
                System.out.println("Date Validation Successful...:)");
            else if (day <= 30 && month != 2)
                System.out.println("Date Validation Successful...:)");
            else
                System.out.println("Date Validation Not successful...:(");
        }
    }
}