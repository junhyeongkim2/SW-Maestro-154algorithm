package DAY8;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.*;

public class BOJ_1168 {
    public static void main(String[] arg) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Queue<Integer> qu = new LinkedList<Integer>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int total = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        StringBuilder sb = new StringBuilder();
        System.out.print("<");
        while(!qu.isEmpty())
        {
            for(int i = 0 ; i < N; i++)
            {
                if(i == N-1) sb.append(qu.poll() + ", ");
                else qu.add(qu.poll());
            }
        }
        System.out.println(sb.substring(0, sb.length()-2) + ">");

    }
}
