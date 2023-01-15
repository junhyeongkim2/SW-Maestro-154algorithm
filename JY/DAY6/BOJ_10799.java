package DAY6;

import java.io.*;
import java.util.*;

public class BOJ_10799 {
    //너무 복잡하게 생각했다. -> 뭔가 조건이 너무 복잡하다고 느껴지면 접근 방법을 다르게 하자
    public static void main(String[] arg) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String g = br.readLine();
        boolean open = false;
        int res = 0;
        LinkedList<Character> list = new LinkedList<>();
        for(int i = 0; i < g.length(); i++)
        {
            char c = g.charAt(i);
            if(c == '(')
            {
                list.addLast(c);
                open = true;
            }
            else if(c == ')')
            {
                list.removeLast();
                if(open)
                {
                    res = res + list.size();
                }
                else
                {
                    res++;
                }
                open = false;


            }

        }
        System.out.println(res);
    }



}
