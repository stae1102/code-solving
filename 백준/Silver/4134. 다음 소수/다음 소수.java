import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        while (n-- > 0) {
            long k = Long.parseLong(br.readLine());
            System.out.println(getPrime(k));
        }
    }

    private static long getPrime(long x) {
        long max = (long) Math.pow(x, 2);
        for (long i = x; i <= max; i++) {
            if (isPrime(i)) {
                return i;
            }
        }
        return 2;
    }

    private static boolean isPrime(long x) {
        if (x < 2) {
            return false;
        }

        for (long i = 2; i <= Math.sqrt(x); i++) {
            if (x % i == 0) {
                return false;
            }
        }
        return true;
    }
}