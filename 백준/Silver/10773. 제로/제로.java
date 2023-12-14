import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Stack stack = new Stack();

        while (n-- > 0) {
            int k = Integer.parseInt(br.readLine());

            if (k != 0) {
                stack.push(k);
            } else {
                stack.pop();
            }
        }
        System.out.println(stack.sum());
    }

    static class Stack {
        private final List<Integer> list = new ArrayList<>();

        public void push(int n) {
            list.add(n);
        }

        public int pop() {
            int lastIndex = list.size() - 1;
            int lastElement = list.get(lastIndex);
            list.remove(lastIndex);

            return lastElement;
        }

        public int sum() {
            int sum = 0;
            for (int e : list) {
                sum += e;
            }

            return sum;
        }
    }
}