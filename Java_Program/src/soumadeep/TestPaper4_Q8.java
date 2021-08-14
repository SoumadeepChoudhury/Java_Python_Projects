package soumadeep;
import java.util.Scanner;
public class TestPaper4_Q8 {
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args) {
        System.out.print("1. BUZZ \n2. GCD \nEnter Choice: ");
        int ch=sc.nextInt();
        switch(ch){
            case 1:
                System.out.print("Enter a number: ");
                int n=sc.nextInt();
                if(n%10==7 || n%7==0)
                    System.out.println("BUZZ Number");
                else 
                    System.out.println("Not BUZZ Number");
                break;
            case 2:
                System.out.print("Entre 2 numbers: ");
                int a=sc.nextInt();
                int b=sc.nextInt();
                int n1,n2;
                if(a>b){
                    n1=a;
                    n2=b;
                }
                else {
                    n1=b;
                    n2=a;
                }

                while(n1%n2!=0){
                    int t=n2;
                    n2=n1%n2;
                    n1=t;
                }

                System.out.println("GCD: "+n2);
                break;
            default: 
                System.out.println("Invalid Choice");
        }
    }
}