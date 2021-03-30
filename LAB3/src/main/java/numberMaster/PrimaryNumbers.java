package numberMaster;

public class PrimaryNumbers {
    public static boolean isPrimary(int number) {
        if (number <= 0) throw new IllegalArgumentException("Illegal number!");
        else if (number == 1) return false;
        for (int i = 2; i < number; i++) {
//            System.out.println(i);
            if (number % i == 0) return false;
        }
        return true;
    }
}
