package soumadeep;

public class TestPaper5_Q8 {
    int Empno;
    String name;
    double salary,hra,da,it,gp;
    void calc(){
        hra=10.0/100*salary;
        da=55.5/100*salary;
        it=6.0/100*salary;
        gp=salary+hra+da-it;
    }
    void unit(){
        Empno=0;
        salary=hra=da=it=gp=0;
        name="";
    }
    void display(){
        System.out.println("\t\tSalary Slip");
        System.out.println("Employee Number: "+Empno+"\nName: "+name+"\nBasic Pay: "+salary+"\nHRA: "+hra+"\nDA: "+da+"\nIT: "+it+"\nGross Pay: "+gp);
    }
    public static void main(String[] args) {
        TestPaper5_Q8 ob=new TestPaper5_Q8();
        ob.unit();
        ob.Empno=45789;
        ob.name="Hello";
        ob.salary=50000;
        ob.calc();
        ob.display();
    }
}