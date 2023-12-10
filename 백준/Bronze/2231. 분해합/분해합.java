import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int constructor = n + 1;

        for (int i = n; i > 0; i--) {
            String s = String.valueOf(i);
            if (sum(s) == n) {
                constructor = Math.min(constructor, Integer.parseInt(s));
            }
        }

        if (constructor != n + 1) {
            System.out.println(constructor);
        } else {
            System.out.println(0);
        }
    }

    private static int sum(String str) {
        int sumValue = Integer.parseInt(str);

        for (int i = 0; i < str.length(); i++) {
            sumValue += Integer.parseInt(String.valueOf(str.charAt(i)));
        }

        return sumValue;
    }
}