import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[3];

        for (int i = 0; i < 3; i++) {
            int angle = Integer.parseInt(br.readLine());
            arr[i] = angle;
        }

        if (Arrays.stream(arr).sum() != 180) {
            System.out.println("Error");
        } else if (isEquilateral(arr)) {
            System.out.print("Equilateral");
        } else if (isIsosceles(arr)) {
            System.out.print("Isosceles");
        } else {
            System.out.print("Scalene");
        }
    }

    private static boolean isEquilateral(int[] arr) {
        return arr[0] == 60 && isIsosceles(arr);
    }

    private static boolean isIsosceles(int[] arr) {
        for (int i = 0; i < 2; i++) {
            for (int j = i + 1; j < 3; j++) {
                if (arr[i] == arr[j]) {
                    return true;
                }
            }
        }
        return false;
    }
}