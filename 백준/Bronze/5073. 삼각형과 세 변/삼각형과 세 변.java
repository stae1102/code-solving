import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == 0 && b == 0 && c == 0) {
                break;
            }

            if (!validate(a, b, c)) {
                System.out.println("Invalid");
            } else if (isEquilateral(a, b, c)) {
                System.out.println("Equilateral");
            } else if (isIsosceles(a, b, c)) {
                System.out.println("Isosceles");
            } else {
                System.out.println("Scalene");
            }
        }
    }

    private static boolean validate(int... intValues) {
        int[] values = max(intValues);
        int index = values[0];
        int value = values[1];

        int shortLineSum = 0;

        for (int i = 0; i < intValues.length; i++) {
            if (i != index) {
                shortLineSum += intValues[i];
            }
        }

        return value < shortLineSum;
    }

    private static int[] max(int... intValues) {
        int maxIndex = 0;
        int maxValue = intValues[0];
        for (int i = 1; i < intValues.length; i++) {
            if (maxValue < intValues[i]) {
                maxIndex = i;
                maxValue = Math.max(maxValue, intValues[i]);
            }
        }
        return new int[] {maxIndex, maxValue};
    }

    private static boolean isEquilateral(int... intValues) {
        return intValues[0] == intValues[1] && intValues[1] == intValues[2];
    }

    private static boolean isIsosceles(int... intValues) {
        return intValues[0] == intValues[1] || intValues[1] == intValues[2] || intValues[0] == intValues[2];
    }
}