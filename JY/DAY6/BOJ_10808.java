package DAY6;
import java.io.*;
import java.util.*;

public class BOJ_10808 {
    public static void main(String[] arg)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int[] al = new int[26];
        String str = br.readLine();
        for(int i = 0; i < str.length(); i++)
        {
            al[str.charAt(i) - 'a']++;
        }
        for(int i = 0; i < al.length; i++)
        {
            sb.append(al[i]).append(" ");
        }
        System.out.println(sb);

    }


}
