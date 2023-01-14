// WAP to convert the Integer to Roman format. Eg: 1234 : MCCXXXIV

// package soumadeep;

import java.util.Scanner;
import java.lang.Math;

class IntToRoman {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.print("Enter Number: ");
        int userInp = sc.nextInt();
        String Roman[] = { "I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M" };
        int Inte[] = { 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000 };
        int noOfDigits = Integer.toString(userInp).length();
        int UserInt[] = new int[noOfDigits];
        int n = userInp;
        int counter = 0;
        String ROMAN = "";
        while (n > 0) { // separating the digits
            UserInt[noOfDigits - counter - 1] = (int) ((n % 10) * Math.pow(10, counter));
            n = (int) n / 10;
            counter++;
        }
        for (int i = 0; i < UserInt.length; i++) { // accessing desired values to convert in Roman
            int start = -1;
            boolean present = false;
            for (int j = 0; j < Inte.length; j++) { // checking for existence and the range
                if (j != Inte.length - 1) {
                    if (UserInt[i] > Inte[j] && UserInt[i] < Inte[j + 1]) {
                        start = j;
                    }
                }
                if (UserInt[i] > Inte[Inte.length - 1]) {
                    start = Inte.length - 1;
                }
                if (UserInt[i] == Inte[j]) {
                    present = true;
                    ROMAN += Roman[j];
                    break;
                }
            }
            if (present == false) {
                int times = 0;
                int index = 0;
                try {
                    int val = Inte[start];
                    String sub = Integer.toString(UserInt[i] - val);
                    int multiple = (int) Math.pow(10, (sub.length() - 1));
                    for (int j = 0; j < Inte.length; j++) {
                        if (multiple == Inte[j]) {
                            index = j;
                        }
                    }
                    times = Integer.parseInt(sub) / multiple;
                    ROMAN += Roman[start];
                } catch (Exception e) {
                    // pass
                }
                for (int j = 0; j < times; j++) {
                    ROMAN += Roman[index];
                }
            }
        }
        System.out.println(ROMAN);
    }
}