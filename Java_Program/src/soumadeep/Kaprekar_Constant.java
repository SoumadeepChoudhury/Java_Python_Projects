package soumadeep;

import java.util.Arrays;
import java.util.Scanner;

public class Kaprekar_Constant {
    final static int CONSTANT = 6174;
    public static void main(String[] args) {
        /*Kaprekar said : Take any 4 digit number
                            Arrange in descending order
                            Then arrange in ascending order
                            Substract the smaller number from bigger number
                            repeat the process.
                            Once you will get the value 6174.
        */
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter 4 digit valid number: ");
        int num1 = sc.nextInt();
        sc.close();
        int counter = 0;
        while(true){
            counter+=1;
            //descending order arrangement
            int decNum = Integer.parseInt(descending(num1));

            //assending order arrangement
            int reversedNum = Integer.parseInt(reverse(String.valueOf(decNum)));


            //substract
            int subsVal = reversedNum>decNum ? reversedNum-decNum : decNum-reversedNum;

            if(subsVal == CONSTANT){
                break;
            }
            num1 = subsVal;
        }
        System.out.println("Number of times needed: "+counter);
    }

    private static String reverse(String num){
        String revNum = "";
        for(int i=num.length()-1;i>=0;i--){
            revNum+=num.charAt(i);
        }
        return revNum;
    }

    private static String descending(int num){
        String decNum = "";

        String[] num_Array = new String[4];
        for(int i=0;i<4;i++){
            num_Array[i] = String.valueOf(num%10);
            num/=10;
        }
        Arrays.sort(num_Array); //ascending
        String temp="";
        for(int i=0;i<num_Array.length;i++){
            temp+=num_Array[i];
        }

        decNum = reverse(temp); //descending


        return decNum;
    }
}