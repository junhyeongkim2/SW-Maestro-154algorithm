package DAY6;

import java.util.*;
import java.io.*;

public class BOJ_9012 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = Integer.parseInt(br.readLine());
        boolean valid = true;
        for(int i = 0; i < total; i++)
        {
            String ps = br.readLine();
            LinkedList<Character> stack = new LinkedList<>();
            for(int j = 0; j < ps.length(); j++)
            {

                char c = ps.charAt(j);
                if(c == '(')
                {
                    stack.addLast(c);
                }
                else
                {
                    if(!stack.isEmpty()) {
                        stack.removeLast();
                    }
                    else
                    {
                        j = ps.length();
                        valid = false;
                        System.out.println(valid);

                    }
                }
            }
            if(!valid)
            {
                System.out.println("NO");
                stack.removeAll(stack);
                valid = true;
            }
            else if(stack.isEmpty())
                System.out.println("YES");
            else {
                System.out.println("NO");
                stack.removeAll(stack);
            }

        }
    }
}
