package DAY1;
import java.io.*;
import java.util.*;
public class BOJ_11021 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());//첫문장
        for(int i = 0; i < num; i++)
        {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            System.out.println("Case #"+(i+1)+": "+ (a+b));
        }


    }
}
