import numberMaster.Vectors;
import org.joml.Vector3f;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class VectorsTest {
    Float delta = 0.001f;

    @Test
    public void vectorLengthIsOne1() {
        Vector3f v = new Vector3f(0.0f, 1.0f, 0.0f);
        assertEquals(Vectors.length(v), 1, delta);
    }

    @Test
    public void vectorLengthIsOne2() {
        Vector3f v = new Vector3f(0.0f, 1.0f, 1.0f);
        assertEquals(Vectors.length(v), 1.414f, delta);
    }

    @Test
    public void vectorLengthIsThree() {
        Vector3f v = new Vector3f(2.0f, 3.0f, 1.0f);
        assertEquals(Vectors.length(v) , 3.7416575f, 0.001);
    }


}
