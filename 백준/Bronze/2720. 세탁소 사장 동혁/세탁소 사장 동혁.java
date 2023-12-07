import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int[] arr = new int[4];
            int money = Integer.parseInt(br.readLine());
            arr[0] = money / 25;
            money %= 25;

            arr[1] = money / 10;
            money %= 10;

            arr[2] = money / 5;
            money %= 5;

            arr[3] = money;

            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < 4; j++) {
                sb.append(arr[j]);
                if (j != 3) {
                    sb.append(" ");
                }
            }
            System.out.println(sb);
        }
    }
}