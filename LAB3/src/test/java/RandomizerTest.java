import static org.junit.Assert.*;

import numberMaster.Fibonacci;
import org.junit.*;
import numberMaster.Randomizer;

public class RandomizerTest {


    @Test
    public void randomNumberisMoreThan70() {
        int result = Randomizer.randomInt(10, 70);
        assertTrue(result < 70);
    }

    @Test
    public void randomNumberIsMoreThan9() {
        int result = Randomizer.randomInt(10, 70);
        assertTrue(result > 9);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testMinusOneExpectedIllegalArgumentException() {
        Randomizer.randomInt(20, -1);
    }


}