import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");

        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        Set<String> strSet = new HashSet<>();

        for (int i = 0; i < n; i++) {
            strSet.add(br.readLine());
        }

        int count = 0;
        for (int i = 0; i < m; i++) {
            if (strSet.contains(br.readLine())) {
                count++;
            }
        }

        System.out.print(count);
    }
}