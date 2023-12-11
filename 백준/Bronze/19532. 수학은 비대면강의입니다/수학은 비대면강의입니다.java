import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        for (int x = -999; x <= 999; x++) {
            for (int y = -999; y <= 999; y++) {
                if (isRoot(x, y, arr)) {
                    System.out.println(x + " " + y);
                    System.exit(0);
                }
            }
        }
    }

    private static boolean isRoot(int x, int y, int[] arr) {
        int a = arr[0], b = arr[1], c = arr[2], d = arr[3], e = arr[4], f = arr[5];

        return (a * x + b * y == c && d * x + e * y == f);
    }
}