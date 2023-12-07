import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            int k = Integer.parseInt(br.readLine());
            if (k == -1) {
                break;
            }

            List<Integer> arr = new ArrayList<>();
            arr.add(1);

            for (int j = 2; j <= Math.sqrt(k); j++) {
                if (k % j == 0) {
                    arr.add(j);
                }
            }

            for (int j = arr.size() - 1; j > 0; j--) {
                int temp = k / arr.get(j);
                if (temp != arr.get(j)) {
                    arr.add(temp);
                }
            }

            if (sum(arr) != k) {
                System.out.println(k + " is NOT perfect.");
                continue;
            }

            System.out.print(k + " = ");

            int length = arr.size();
            for (int j = 0; j < length; j++) {
                System.out.print(arr.get(j));
                if (j != length - 1) {
                    System.out.print(" + ");
                }
            }
            System.out.println();
        }
    }

    private static int sum(List<Integer> arr) {
        return arr.stream().mapToInt(Integer::intValue).sum();
    }
}