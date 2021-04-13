import static org.junit.Assert.*;

import org.junit.*;
import numberMaster.PrimaryNumbers;

public class PrimaryNumbersTest {

    @Test
    public void testThreeIsPrimarySameAsTrue() {
        assertSame( PrimaryNumbers.isPrimary(3), true);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testMinusOneExpectedIllegalArgumentException() {
        PrimaryNumbers.isPrimary(-1);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testZeroExpectedIllegalArgumentException() {
        PrimaryNumbers.isPrimary(0);
    }

    @Test
    public void testOneIsNotPrimaryNumber() {
        boolean result = PrimaryNumbers.isPrimary(1);
        assertFalse(result);
    }

    @Test
    public void testTwoIsPrimaryNumber() {
        boolean result = PrimaryNumbers.isPrimary(2);
        assertTrue(result);
    }

    @Test
    public void testThreeIsPrimaryNumber() {
        boolean result = PrimaryNumbers.isPrimary(3);
        assertTrue(result);
    }

    @Test
    public void testFourIsNotPrimaryNumber() {
        boolean result = PrimaryNumbers.isPrimary(4);
        assertFalse(result);
    }

    @Test
    public void testFiveIsPrimaryNumber() {
        boolean result = PrimaryNumbers.isPrimary(5);
        assertTrue(result);
    }

    @Test
    public void testTenIsNotPrimaryNumber() {
        boolean result = PrimaryNumbers.isPrimary(10);
        assertFalse(result);
    }

    @Test
    public void testElevenIsPrimaryNumber() {
        boolean result = PrimaryNumbers.isPrimary(11);
        assertTrue(result);
    }

    @Test
    public void testThirteenIsPrimaryNumber() {
        boolean result = PrimaryNumbers.isPrimary(13);
        assertTrue(result);
    }
}