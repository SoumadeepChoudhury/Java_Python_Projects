package soumadeep;
import java.util.Scanner;
public class ReverseString {
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("Enter Sentence: ");
        String s=sc.nextLine();
        s+=" ";
        String s1="";
        int p=0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)==32){
                s1=s.substring(p, i);
                p=i+1;
                for(int j=s1.length()-1;j>=0;j--){
                    System.out.print(s1.charAt(j));
                }
                System.out.print(" ");
            }
        }

        for(int i=s.trim().length()-1;i>=0;i--){
            System.out.print(s.charAt(i));
        }
        s=" "+s.trim();
        p=s.length();
        for(int i=s.length()-1;i>=0;i--){
            if(s.charAt(i)==32){
                s1=s.substring(i+1, p);
                p=i;               
                    System.out.print(s1+" ");                     
            }
        }
    }
}