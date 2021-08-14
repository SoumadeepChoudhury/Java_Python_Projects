package soumadeep;

import java.util.Date;
import java.util.Scanner;

public class AgeYearCalculator {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Enter your age: ");
        int age = sc.nextInt();
        System.out.println("Enter final age: ");
        int final_age = sc.nextInt();
        Date date = new Date();
        @SuppressWarnings("deprecation")
        int current_year = date.getYear() + 1900;
        int age_difference = final_age - age;
        if (final_age > age)
            System.out.println("Year in which you will get " + final_age + " is " + (current_year + age_difference));
        else
            System.out.println("Year in which you were " + final_age + " 1is " + (current_year + age_difference));
    }
}