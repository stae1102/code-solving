import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] a = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int a1 = a[0];
        int a0 = a[1];

        int c = Integer.parseInt(br.readLine());
        int n0 = Integer.parseInt(br.readLine());

        int firstValue = (c * n0) - (a1 * n0 + a0);

        if (firstValue < 0) {
            System.out.println(0);
        } else {
            int secondValue = (c * (n0 + 1)) - (a1 * (n0 + 1) + a0);

            boolean isNotDecrement = secondValue - firstValue >= 0;
            if (isNotDecrement) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }
}