import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int k = 0;

        while (true) {
            if (isPackable(n, k)) {
                System.out.println((n - (3 * k)) / 5 + k);
                break;
            }

            if (3 * k > n) {
                System.out.println(-1);
                break;
            }

            k++;
        }
    }

    private static boolean isPackable(int n, int k) {
        return (n - (3 * k)) % 5 == 0;
    }
}