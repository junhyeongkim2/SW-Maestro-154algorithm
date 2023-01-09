package DAY3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ10866 {
    private static int[] deque = new int[10001];
    private static int idx = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            // set instruction
            String instruction = st.nextToken();

            // execute instruction
            if (instruction.equals("push_front")) {
                push_front(Integer.parseInt(st.nextToken()));
            } else if (instruction.equals("push_back")) {
                push_back(Integer.parseInt(st.nextToken()));
            } else if (instruction.equals("pop_front")) {
                System.out.println(pop_front());
            } else if (instruction.equals("pop_back")) {
                System.out.println(pop_back());
            } else if (instruction.equals("size")) {
                System.out.println(size());
            } else if (instruction.equals("empty")) {
                System.out.println(empty());
            } else if (instruction.equals("front")) {
                System.out.println(front());
            } else if (instruction.equals("back")) {
                System.out.println(back());
            } else {
                System.out.println("input error");
                return;
            }
        }
    }

    private static void push_front(int num) {
        if(idx == 0){
            deque[idx++] = num;
            return;
        }

        for(int i = idx-1; i >= 0; i--){
            deque[i+1] = deque[i];
        }
        deque[0] = num;
        idx++;
    }

    private static void push_back(int num) {
        deque[idx++] = num;
    }

    private static int pop_front() {
        if (idx == 0)
            return -1;

        int answer = deque[0];

        // 요소들 앞으로 땡기기
        for (int i = 1; i < idx; i++) {
            deque[i - 1] = deque[i];
        }
        idx--;

        return answer;
    }

    private static int pop_back() {
        if (idx == 0)
            return -1;

        return deque[--idx];
    }

    private static int size() {
        return idx;
    }

    private static int empty() {
        return (idx == 0) ? 1 : 0;
    }

    private static int front() {
        return (idx == 0) ? -1 : deque[0];
    }

    private static int back() {
        return (idx == 0) ? -1 : deque[idx - 1];
    }
}


/*
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
 */