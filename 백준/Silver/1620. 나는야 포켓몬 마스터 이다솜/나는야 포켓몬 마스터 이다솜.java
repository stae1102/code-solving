import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        Map<String, Integer> pocketmon = new HashMap<>();
        Map<Integer, String> pocketmonIdx = new HashMap<>();


        for (int i = 1; i <= n; i++) {
            String input = br.readLine();
            pocketmon.put(input, i);
            pocketmonIdx.put(i, input);
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            String command = br.readLine();
            try {
                int k = Integer.parseInt(command);
                sb.append(pocketmonIdx.get(k));
            } catch (Exception e) {
                sb.append(pocketmon.get(command));
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
