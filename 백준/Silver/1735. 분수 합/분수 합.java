import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int a1 = Integer.parseInt(st.nextToken());
        int a2 = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int b1 = Integer.parseInt(st.nextToken());
        int b2 = Integer.parseInt(st.nextToken());

        int gcd;

        if (a2 > b2) {
            gcd = gcd(a2, b2);
        } else {
            gcd = gcd(b2, a2);
        }

        int lcm = lcm(gcd, a2, b2);

        int aTemp = (lcm / a2);
        a1 *= aTemp; a2 *= aTemp;

        int bTemp = (lcm / b2);
        b1 *= bTemp; b2 *= bTemp;

        int c1 = a1 + b1;
        int c2 = lcm;

        int cGcd;
        if (c1 > c2) {
            cGcd = gcd(c1, c2);
        } else {
            cGcd = gcd(c2, c1);
        }

        System.out.println((c1 / cGcd) + " " + (c2 / cGcd));
    }

    private static int gcd(int x, int y) {
        int temp = x % y;

        if (temp == 0) {
            return y;
        } else {
            return gcd(y, temp);
        }
    }

    private static int lcm(int gcd, int x, int y) {
        return gcd * (x / gcd) * (y / gcd);
    }
}