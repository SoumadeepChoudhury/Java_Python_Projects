package soumadeep;
import java.util.Scanner;
public class TestPaper3_Q5 {
    static Scanner sc=new Scanner(System.in);
    public static void main(String args[]) {
        int p[]=new int[6];
        int q[]=new int[4];
        for(int i=0;i<6;i++){
            System.out.print("Enter value "+(i+1)+" : ");
            p[i]=sc.nextInt();
        }

        for(int i=0;i<4;i++){
            System.out.print("Enter value "+(i+1)+" : ");
            q[i]=sc.nextInt();
        }

        int r[]=new int[10];
        for(int i=0;i<10;i++){
            if(i<6)
                r[i]=p[i];
            else
                r[i]=q[i-6];
        }

        for(int i=0;i<10;i++){
            System.out.print(r[i]+", ");            
        }
    }
}