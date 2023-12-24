import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int gcd;

        if (a > b) {
            gcd = gcd(a, b);
        } else {
            gcd = gcd(b, a);
        }

        long answer = (long) gcd * (a / gcd) * (b / gcd);

        System.out.println(answer);
    }

    private static int gcd(int x, int y) {
        int temp = x % y;

        if (temp == 0) {
            return y;
        } else {
            return gcd(y, temp);
        }
    }
}