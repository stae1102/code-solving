import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arr = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int value = max(arr)[1];
        int sum = Arrays.stream(arr).sum();

        if (validate(arr)) {
            System.out.println(Arrays.stream(arr).sum());
        } else {
            System.out.println((sum - value) * 2 - 1);
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
}