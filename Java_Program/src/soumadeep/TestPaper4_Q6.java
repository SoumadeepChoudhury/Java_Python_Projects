package soumadeep;
public class TestPaper4_Q6 {
    void compare(int x,int x1){
        System.out.println((int)Math.max(x, x1));
    }

    void compare(char c,char c1){
        System.out.println((char)Math.max(c, c1));
    }

    void compare(String x, String x1){
        System.out.println(x.length()>x1.length()?x:x1);
    }
    public static void main(String[] args) {
        TestPaper4_Q6 ob=new TestPaper4_Q6();
        ob.compare(4, 8);
        ob.compare('X', 'Z');
        ob.compare("HelloVSCode", "HelloEclipse");
    }
}