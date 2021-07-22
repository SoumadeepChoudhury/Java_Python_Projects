package soumadeep;
import java.util.Scanner;
public class TestPaper5_Q7 {
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args) {
        System.out.print("Enter a number: ");
        int n=sc.nextInt();
        int n1=n,s=0;
        while(n>0){
            int d=n%10;
            int f=1;
            for(int i=1;i<=d;i++)
                f*=i;
            s+=f;
            n/=10;
        }
        if(s==n1)
            System.out.println("Special Number");
        else
            System.out.println("Not Special Number");
    }
}