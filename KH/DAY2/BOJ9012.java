package DAY2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.EmptyStackException;
import java.util.Stack;
import java.util.StringTokenizer;

public class BOJ9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String parenthesis = st.nextToken();

            // check
            System.out.println((checkVPS(parenthesis)) ? "YES" : "NO");
        }
    }

    private static boolean checkVPS(String str) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();

        // set stack
        for(int i = 0 ; i < str.length(); i++){
            char ch = str.charAt(i);
            if(ch == '(')
                stack.push(ch);
            else{
                try{
                    if(ch == ')')
                        stack.pop();
                }catch(EmptyStackException e){
                    return false;
                }
            }
        }

        if(!stack.isEmpty())
            answer = false;

        return answer;
    }
}

