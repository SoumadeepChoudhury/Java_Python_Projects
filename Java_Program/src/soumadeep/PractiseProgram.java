// Fibonacci Series using recursion.0,1,1,2,3,5,8,13,21,34

package soumadeep;

import java.io.*;

public class PractiseProgram {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int a = 0, b = 1, c;

    public static void main(String[] args) throws IOException {
        System.out.println("Enter no. of terms: ");
        int n = Integer.parseInt(br.readLine());
        if (n > 1) {
            System.out.print("0, 1, ");
            fib(n -= 2);
        } else
            System.out.println("Require at least three terms..");
    }

    static void fib(int n) {
        if (n > 0) {
            c = a + b;
            if (n != 1)
                System.out.print(c + ", ");
            else
                System.out.println(c);
            a = b;
            b = c;
            fib(--n);
        }
    }
}