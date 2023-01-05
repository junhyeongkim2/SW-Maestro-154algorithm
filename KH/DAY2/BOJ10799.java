package DAY2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class BOJ10799 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String parenthesis = br.readLine();

        // 계산
        int answer = 0;
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < parenthesis.length(); i++) {
            char ch = parenthesis.charAt(i);
            if(ch == '(')
                stack.push('(');
            else if(ch == ')'){
                stack.pop();
                // laser
                if(parenthesis.charAt(i-1) == '(')
                    answer += stack.size();
                // 막대 끝
                else answer += 1;
            }
        }

        System.out.println(answer);
    }
}
