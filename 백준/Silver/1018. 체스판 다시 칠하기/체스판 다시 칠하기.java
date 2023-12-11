import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] s = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = s[0];
        int m = s[1];

        String[][] chess = new String[n][m];

        for (int i = 0; i < n; i++) {
            String[] row = br.readLine().split("");
            chess[i] = row;
        }

        int answer = -1;
        for (int i = 0; i <= n - 8; i++) {
            for (int j = 0; j <= m - 8; j++) {
                int incorrect = findIncorrect(i, j, chess);
                if (answer == -1) {
                    answer = incorrect;
                } else {
                    answer = Math.min(answer, incorrect);
                }
            }
        }
        System.out.println(answer);
    }

    private static int findIncorrect(int n, int m, String[][] chess) {
        int wCount = 0;
        int bCount = 0;
        // 좌상단이 W인 경우
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if ((i + j) % 2 == 0 && chess[n + i][m + j].equals("W")) {
                    wCount++;
                } else if ((i + j) % 2 == 1 && chess[n + i][m + j].equals("B")) {
                    bCount++;
                }
            }
        }

        int answer1 = 64 - (wCount + bCount);

        wCount = 0;
        bCount = 0;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if ((i + j) % 2 == 0 && chess[n + i][m + j].equals("B")) {
                    bCount++;
                } else if ((i + j) % 2 == 1 && chess[n + i][m + j].equals("W")) {
                    wCount++;
                }
            }
        }

        int answer2 = 64 - (wCount + bCount);
        return Math.min(answer1, answer2);
    }
}