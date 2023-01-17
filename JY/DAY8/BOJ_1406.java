package DAY8;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class BOJ_1406 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        Stack<Character> left = new Stack<>();
        Stack<Character> right = new Stack<>();
        int total = Integer.parseInt(br.readLine());
        StringTokenizer st;

        for(int i = 0; i < str.length();i++)
        {
            left.push(str.charAt(i));
        }
        for(int i = 0 ; i < total; i++)
        {
            st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            if(s.equals("L")){
                if(!left.isEmpty()) right.push(left.pop());

            }
            else if(s.equals("D")){
                if(!right.isEmpty()) left.push(right.pop());

            }
            else if(s.equals("B"))
            {
                if(!left.isEmpty()) left.pop();

            }
            else if(s.equals("P")){
                left.add(st.nextToken().charAt(0));
            }
        }
        while(!left.isEmpty())
        {
            right.push(left.pop());
        }
        StringBuilder sb = new StringBuilder();
        while(!right.isEmpty()){
            sb.append(right.pop());
        }
        System.out.println(sb);


    }
}
