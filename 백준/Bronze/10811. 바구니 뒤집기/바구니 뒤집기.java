import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arr = initIntArray(0, n);

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            int tempN = b - a + 1;
            int[] temp = new int[tempN];
            for (int j = 0; j < tempN; j++) {
                temp[j] = arr[a + j];
            }

            for (int j = a; j <= b; j++, tempN--) {
                arr[j] = temp[tempN - 1];
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            sb.append(arr[i]).append(" ");
        }

        System.out.print(sb);
    }

    private static int[] initIntArray(int start, int end) {
        int[] arr = new int[end - start + 1];
        for (int i = 1; i <= end; i++) {
            arr[i] = i;
        }

        return arr;
    }
}