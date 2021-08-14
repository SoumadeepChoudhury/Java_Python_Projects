package soumadeep;
import java.util.Scanner;
public class TestPaper5_Q4 {
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args) {
        String n[]=new String[15];
        double ta[]=new double[15];
        double d[]=new double[15];

        for(int i=0;i<15;i++){
            System.out.print("Enter Name: ");
            n[i]=sc.next();
            System.out.print("Ticket Charge: ");
            ta[i]=sc.nextDouble();

            if(ta[i]>70000)
                d[i]=18.0/100*ta[i];
            else if(ta[i]>55000 && ta[i]<=70000)
                d[i]=16.0/100*ta[i];
            else if(ta[i]>35000 && ta[i]<=55000)
                d[i]=12.0/100*ta[i];
            else if(ta[i]>25000 && ta[i]<=35000)
                d[i]=10.0/100*ta[i];
            else if(ta[i]<=25000)
                d[i]=0.0;

        }
        System.out.println("S. No\t Name \t Ticket Charge \t🤔Discount \t Net Amount");
        for(int i=0;i<15;i++){
            System.out.println((i+1)+"\t"+n[i]+"\t"+ta[i]+"\t"+d[i]+"\t"+(ta[i]-d[i]));
        }
        
    }
}