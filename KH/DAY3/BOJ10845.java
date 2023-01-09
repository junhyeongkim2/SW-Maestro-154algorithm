package DAY3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ10845 {
    private static int[] queue = new int[10001];
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

    private static void push(int num) {
        queue[idx++] = num;
    }


    private static int pop() {
        if(idx == 0)
            return -1;

        int answer = queue[0];

        // 요소들 앞으로 땡기기
        for(int i = 1; i < idx; i++){
            queue[i-1] = queue[i];
        }
        idx--;

        return answer;
    }

    private static int size(){
        return idx;
    }

    private static int empty() {
        return (idx == 0) ? 1 : 0;
    }

    private static int front() {
        return (idx == 0) ? -1 : queue[0];
    }

    private static int back() {
        return (idx == 0) ? -1 : queue[idx-1];
    }

}


/*
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
 */