import java.math.BigInteger;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        Long start = System.currentTimeMillis();

        PrimeGenerator primeGenerator = new PrimeGenerator();
        List<BigInteger> results = primeGenerator.getPrimes(100);
        Long end = System.currentTimeMillis();
        System.out.println("The time taken was " + (end - start) + " ms.");
        if (!results.isEmpty()) {
            System.out.println("The first number found was : " + results.get(0));
        } else {
            System.out.println("No prime numbers were found.");
        }
    }
}