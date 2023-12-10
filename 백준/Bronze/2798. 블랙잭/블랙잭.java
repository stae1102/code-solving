import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] card = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int maxValue = -1;

        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    int sum = card[i] + card[j] + card[k];
                    if (sum == m) {
                        System.out.println(sum);
                        System.exit(0);
                    } else if (sum < m) {
                        maxValue = Math.max(maxValue, sum);
                    }
                }
            }
        }

        System.out.println(maxValue);
    }
}