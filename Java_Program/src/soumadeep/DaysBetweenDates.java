// Program to calculate number of days between two dates

package soumadeep;

import java.util.Scanner;

public class DaysBetweenDates {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter first date in dd/mm/yyyy: ");
        String date1 = sc.nextLine();
        System.out.print("Enter second date in dd/mm/yyyy: ");
        String date2 = sc.nextLine();

        int day1 = Integer.parseInt(date1.substring(0, 2));
        int month1 = Integer.parseInt(date1.substring(3, 5));
        int year1 = Integer.parseInt(date1.substring(6));

        int day2 = Integer.parseInt(date2.substring(0, 2));
        int month2 = Integer.parseInt(date2.substring(3, 5));
        int year2 = Integer.parseInt(date2.substring(6));

        int day = day2 - day1;
        int month = month2 - month1;
        int year = year2 - year1;

        int total_days = day + (month * 30) + (year * 365);

        System.out.println("Total No of days: " + total_days);
    }
}
