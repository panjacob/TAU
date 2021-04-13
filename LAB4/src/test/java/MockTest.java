import static org.junit.Assert.*;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;
import static org.mockito.BDDMockito.*;
import numberMaster.PrimaryNumbers;

import numberMaster.Fibonacci;
import numberMaster.Randomizer;
import numberMaster.RandomizerInterface;
import org.junit.*;


public class MockTest {
    @Test
    public void testOneFibEqualsFifteen() {
        Fibonacci fib = mock(Fibonacci.class);
        when(fib.fib2(1)).thenReturn(15);
        int result = fib.fib2(1);
        assertEquals(15, result);
    }

    @Test
    public void testOneFibEqualsSomeString() {
        Fibonacci fib = mock(Fibonacci.class);
        given(fib.fib2(1)).willReturn(13);
        int result = fib.fib2(1);
        assertEquals(13, result);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testOneFibThrowsError() {
        Fibonacci fib = mock(Fibonacci.class);
        given(fib.fib2(1)).willThrow(new IllegalArgumentException("Illegal number!"));
        fib.fib2(1);
    }

    @Test
    public void testEchoReturnsSomethingDifferent() {
        Fibonacci fib = mock(Fibonacci.class);
        given(fib.echo("Hello world!")).willReturn(("Goodbye world?"));
        assertEquals(fib.echo("Hello world!"), "Goodbye world?");
    }

    @Test
    public void testTwoIsPrimaryNumber() {
        PrimaryNumbers primaryNumbers = mock(PrimaryNumbers.class);
        given(primaryNumbers.isPrimary2(2)).willReturn(false);
        boolean result = primaryNumbers.isPrimary2(2);
        assertFalse(result);
    }

    @Test(expected = IllegalAccessError.class)
    public void testTwoThrowsIllegalAccessError() {
        PrimaryNumbers primaryNumbers = mock(PrimaryNumbers.class);
        given(primaryNumbers.isPrimary2(2)).willThrow(new IllegalAccessError("abc"));
        primaryNumbers.isPrimary2(2);
    }

    @Test(expected = IllegalThreadStateException.class)
    public void testTwoThrowsIllegalThreadStateException() {
        PrimaryNumbers primaryNumbers = mock(PrimaryNumbers.class);
        given(primaryNumbers.isPrimary2(2)).willThrow(new IllegalThreadStateException("abc"));
        primaryNumbers.isPrimary2(2);
    }

    @Test
    public void randomizerAndRandomizerStubReturnsDifferentResults() {
        RandomizerInterface randomizer = new Randomizer();
        RandomizerInterface randomizerStub = new RandomizerStub();
        int start = 10;
        int end = 70;
        int result = randomizer.randomInt2(start, end);
        int resultStub = randomizerStub.randomInt2(start, end);
        assertTrue(result != resultStub);
    }




}
