package DAY2;

import java.io.*;
import java.util.*;
public class BOJ_1463 {

    public static void main(String[] arg) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = Integer.parseInt(br.readLine());
        int dp[] = new int[total + 1];
        dp[0] = 0;
        dp[1] = 0;

        for(int i = 2; i <= total; i++)
        {
            dp[i] = dp[i-1] + 1;
            if (i % 2 == 0) dp[i] = Math.min(dp[i], dp[i/2] + 1);
            if (i % 3 == 0) dp[i] = Math.min(dp[i], dp[i/3] + 1);

        }
        System.out.println(dp[total]);

    }

}
