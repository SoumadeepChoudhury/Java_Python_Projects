package soumadeep;
import java.util.Scanner;
public class TestPaper3_Q6 {
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("Enter choice: \n1. Series. \n2. Sum of Series.");
        int ch=sc.nextInt();
        switch(ch){
            case 1:
                System.out.print("Enter n: ");
                int n=sc.nextInt();
                for(int i=1;i<=n;i++){
                    System.out.print(i*i-1+", ");
                }
                break;
            case 2:
                double sum=0;
                for(int i=2;i<=20;i++){
                    sum+=(i-1)*1.0/i;
                }
                System.out.println("Sum: "+sum);
                break;
            default:
                System.out.println("Invalid Choice");
    }
}
}