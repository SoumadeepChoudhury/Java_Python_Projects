package soumadeep;
import java.util.Scanner;
public class TestPaper5_Q5 {
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args) {
        int n[]=new int[5];
        double m1[]=new double[5];
        double m2[]=new double[5];
        double m3[]=new double[5];
        double av[]=new double[5];
        for(int i=0;i<5;i++){
            System.out.print("Enter Roll No. : ");
            n[i]=sc.nextInt();
            System.out.print("Marks in three subjects: ");
            m1[i]=sc.nextDouble();
            m2[i]=sc.nextDouble();
            m3[i]=sc.nextDouble();
            av[i]=(m1[i]+m2[i]+m3[i])/3;
        }       
        //a)
        System.out.println("Average of all students");
        for(int i=0;i<5;i++){
            System.out.println(av[i]);
        }
        //b)
        System.out.println("Students whose average is above 80");
        for(int i=0;i<5;i++){
            if(av[i]>80)
            System.out.println(n[i]+"\t"+av[i]);
        }
        //c)
        System.out.println("Stusents whose average is below 40");
        for(int i=0;i<5;i++){
            if(av[i]<40)
            System.out.println(n[i]+"\t"+av[i]);
        }
    }
}