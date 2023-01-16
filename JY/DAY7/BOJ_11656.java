package DAY7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_11656 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String str = br.readLine();
        String[] res = new String[str.length()];
        for(int i =0; i < str.length(); i++)
        {
            res[i] = str.substring(i);
        }
        Arrays.sort(res);
        for(int i = 0; i < res.length; i++)
        {
            sb.append(res[i]).append("\n");
        }
        System.out.println(sb);
    }
    }
