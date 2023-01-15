package DAY6;

import java.io.*;import java.util.*;

public class BOJ_10845 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = Integer.parseInt(br.readLine());
        StringTokenizer st;
        LinkedList<Integer> list = new LinkedList<>();
        for(int i = 0; i < total; i++)
        {
            st = new StringTokenizer(br.readLine());
            String com = st.nextToken();
            if(com.equals("push")){
                list.offer(Integer.parseInt(st.nextToken()));

            }
            else if(com.equals("pop"))
            {
                if(list.isEmpty()) System.out.println(-1);
                else System.out.println(list.poll());

            }
            else if(com.equals("size")){
                System.out.println(list.size());
            }
            else if(com.equals("empty"))
            {
                if(list.isEmpty()) System.out.println(1);
                else System.out.println(0);
            }
            else if(com.equals("front"))
            {
                if(list.isEmpty()) System.out.println(-1);
                else System.out.println(list.getFirst());

            }
            else if(com.equals("back"))
            {
                if(list.isEmpty()) System.out.println(-1);
                else System.out.println(list.getLast());

            }
        }


    }
}
