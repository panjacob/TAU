package numberMaster;

public class Fibonacci {
    public static int fib(int n) {
        if (n <= 0) throw new IllegalArgumentException("Illegal number!");
        else if ((n == 1) || (n == 2)) return 1;
        else return fib(n - 1) + fib(n - 2);
    }
}
