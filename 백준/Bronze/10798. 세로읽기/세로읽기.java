import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[][] words = new String[5][15];
        int maxLength = -1;

        for (int i = 0; i < 5; i++) {
            String[] arr = br.readLine().split("");
            if (arr.length > maxLength) {
                maxLength = arr.length;
            }
            for (int j = 0; j < arr.length; j++) {
                words[i][j] = arr[j];
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < maxLength; i++) {
            for (int j = 0; j < 5; j++) {
                if (words[j][i] != null) {
                    sb.append(words[j][i]);
                }
            }
        }
        System.out.println(sb);
    }
}