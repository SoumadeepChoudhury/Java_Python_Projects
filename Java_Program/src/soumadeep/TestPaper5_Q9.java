package soumadeep;
import java.util.Scanner;
public class TestPaper5_Q9 {
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args) {
        System.out.print("Enter a number: ");
        int n=sc.nextInt();
        System.out.print("1. Prime\n2. Automorphic \nEnter Choice: ");
        int ch=sc.nextInt();
        switch(ch){
            case 1:
                int c=0;
                for(int i=1;i<=n;i++)
                    if(n%i==0)
                        c++;
                if(c==2)
                    System.out.println("Prime Number");
                else
                    System.out.println("Not Prime Number");
                break;
            case 2:
                int n1=n;
                int sq=(int)Math.pow(n,2);
                int d=0;
                while(n>0){
                    d++;
                    n/=10;
                }
                int div=(int)Math.pow(10, d);
                if(sq%div==n1)
                    System.out.println("Automorphic Number");
                else
                    System.out.println("Not Automorphic Number");
                break;
            default:
                System.out.println("Invalid Choice");
        }
    }
}