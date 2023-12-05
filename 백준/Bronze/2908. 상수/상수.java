import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String[] a = st.nextToken().split("");
        String[] b = st.nextToken().split("");

        StringBuilder sb = new StringBuilder();
        for (String s : a) {
            sb.append(s);
        }
        int reversedA = Integer.parseInt(sb.reverse().toString());

        sb = new StringBuilder();
        for (String s : b) {
            sb.append(s);
        }
        int reversedB = Integer.parseInt(sb.reverse().toString());

        System.out.print(Math.max(reversedA, reversedB));
    }
}
