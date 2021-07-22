package soumadeep;
import java.util.Scanner;
public class TestPaper4_Q9 {
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args) {
        // a... Sum=24+6-8.......-20

        double sum=0;
        int k=2;
        for(int i=2;i<=20;i+=2)
            sum+=i*Math.pow(-1, k++);
                   
        System.out.println("Sum: "+sum);

        sum=0;

        // b... Sum = x/2 + x/5 + x/8 ... + x/20
        System.out.println("Enter x: ");
        double x=sc.nextDouble();
        for(int i=2;i<=20;i+=3)
            sum+=x/i;
        
            System.out.println("Sum : "+sum);
    }
}