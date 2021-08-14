package soumadeep;
import java.util.Scanner;
public class TestPaper4_Q5 {
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args) {
        System.out.print("Enter input: ");
        int n=sc.nextInt();
        System.out.print("1. Palindrome \n2. Perfect. \nWhich one to check? ");
        int ch=sc.nextInt();
        switch(ch){
            case 1:
                int x=0,n1=n;
                while(n>0){
                    int d=n%10;
                    x=10*x+d;
                    n/=10;
                }
                if(n1==x)
                    System.out.println("Palindrome");
                else 
                    System.out.println("Not Palindrome");
                break;
            case 2:
                int s=0;
                for(int i=1;i<n;i++){
                    if(n%i==0)
                        s+=i;
                }
                if(s==n)
                    System.out.println("Perfect Number");
                else 
                    System.out.println("Not Perfect Number");
                break;
            default:
                System.out.println("Invaild choice");
        }
    }
}