package soumadeep;

public class TestPaper3_Q8 {
    void num_calc(int num,char ch){
        if(ch=='s')
            System.out.println("Square: "+num*num);
        else
        System.out.println("Cube: "+num*num*num);
    }

    void num_calc(int a,int b,char ch){
        if(ch=='p')
            System.out.println("Product: "+a*b);
        else
            System.out.println("Add: "+a+b);
    }

    void num_calc(String s1,String s2){
        if(s1.equals(s2))
            System.out.println("Equals");
        else
            System.out.println("Not Equals");
    }
    public static void main(String[] args) {
        TestPaper3_Q8 ob=new TestPaper3_Q8();
        ob.num_calc(5, 'x');
        ob.num_calc(3, 39, 'z');
        ob.num_calc("Hello", "HELLO");
    }
    
}