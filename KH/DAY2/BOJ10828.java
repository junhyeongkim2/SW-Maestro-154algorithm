package DAY2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ10828 {
    private static int[] stack = new int[10001];
    private static int idx = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            // set instruction
            String instruction = st.nextToken();

            // execute instruction
            if (instruction.equals("push")) {
                push(Integer.parseInt(st.nextToken()));
            } else if (instruction.equals("pop")) {
                System.out.println(pop());
            } else if (instruction.equals("size")) {
                System.out.println(size());
            } else if (instruction.equals("empty")) {
                System.out.println(empty());
            } else if (instruction.equals("top")) {
                System.out.println(top());
            } else {
                System.out.println("input error");
                return;
            }
        }
    }

    private static void push(int num) {
        stack[idx++] = num;
    }


    private static int pop() {
        if (idx == 0)
            return -1;

        return stack[--idx];
    }

    private static int size() {
        return idx;
    }

    private static int empty() {
        return (idx == 0) ? 1 : 0;
    }

    private static int top() {
        if(idx == 0)
            return -1;

        return stack[idx-1];
    }

}
