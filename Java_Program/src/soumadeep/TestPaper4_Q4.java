package soumadeep;
import java.util.Scanner;
public class TestPaper4_Q4 {
    static Scanner sc=new Scanner(System.in);
    public static void main(String[] args) {
        System.out.print("Enter name: ");
        String name=sc.next();
        System.out.print("Enter address: ");
        String add=sc.next();
        System.out.print("Enter amount of puchase: ");
        double a=sc.nextDouble();
        System.out.print("Enter tyoe of purchase(L/D): ");
        char c=sc.next().charAt(0);
        
        double amount=0;
        if(c=='L'){
            if(a<=25000)
                amount = a;
            else if(a>25000 && a<=57000)
                amount=a-(5.0/100*a);
            else if(a>57000 && a<=100000)
                amount =a-(7.5/100*a);
            else
                amount=a-(10.0/100*a);
        }
        else if(c=='D'){
            if(a<=25000)
                amount = a-(5.0/100*a);
            else if(a>25000 && a<=57000)
                amount=a-(7.5/100*a);
            else if(a>57000 && a<=100000)
                amount =a-(10.0/100*a);
            else
                amount=a-(15.0/100*a);
        }
        else 
            System.out.println("Invalid Type");

        System.out.println("Name: "+name+"\nAddress: "+add+"\nNet Amount to be paid: "+amount);
    }
}