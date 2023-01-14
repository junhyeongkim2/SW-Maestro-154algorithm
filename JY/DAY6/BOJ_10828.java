package DAY6;

import java.io.*;
import java.util.*;

public class BOJ_10828 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = Integer.parseInt(br.readLine());
        StringTokenizer st;
        LinkedList<Integer> list = new LinkedList<>();
        for(int i = 0; i < total; i++)
        {
            st = new StringTokenizer(br.readLine());
            String coman = st.nextToken();
            if(coman.equals("push")){
                int num = Integer.parseInt(st.nextToken());
                list.addLast(num);

            }
            else if(coman.equals("pop"))
            {
                if(list.isEmpty()) System.out.println(-1);
                else System.out.println(list.removeLast());
            }
            else if(coman.equals("size"))
            {
                System.out.println(list.size());
            }
            else if(coman.equals("empty"))
            {
                if(list.isEmpty()) System.out.println(1);
                else System.out.println(0);
            }
            else if(coman.equals("top"))
            {
                if(list.isEmpty()) System.out.println(-1);
                else System.out.println(list.getLast());
            }
        }
    }
}
