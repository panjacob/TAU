package numberMaster;

import org.apache.commons.math3.random.ISAACRandom;
import org.apache.commons.math3.random.RandomGenerator;


public class Randomizer {



    public static int randomInt(int start, int end) {
        RandomGenerator test = new ISAACRandom(44565656);
        return test.nextInt(end) + start;
    }
}
