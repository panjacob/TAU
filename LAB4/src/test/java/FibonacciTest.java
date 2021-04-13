import static org.junit.Assert.*;

import org.junit.*;
import numberMaster.Fibonacci;

public class FibonacciTest {

    @Test(expected = IllegalArgumentException.class)
    public void testMinusOneExpectedIllegalArgumentException() {
        Fibonacci.fib(-1);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testZeroExpectedIllegalArgumentException() {
        Fibonacci.fib(0);
    }

    @Test
    public void testOneFibEqualsOne() {
        int result = Fibonacci.fib(1);
        assertEquals(result, 1);
    }

    @Test
    public void testTwoFibEqualsOne() {
        int result = Fibonacci.fib(2);
        assertEquals(result, 1);
    }

    @Test
    public void testThreeFibEqualsThree() {
        int result = Fibonacci.fib(2);
        assertEquals(result, 1);
    }

    @Test
    public void testTenFibEqualsFiftyFive() {
        int result = Fibonacci.fib(10);
        assertEquals(result, 55);
    }

    @Test
    public void testFibEquals17711() {
        int result = Fibonacci.fib(22);
        assertEquals(result, 17711);
    }


}