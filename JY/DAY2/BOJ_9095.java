package DAY2;

import java.io.*;
import java.util.*;
public class BOJ_9095 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = Integer.parseInt(br.readLine());

        int[] dp = new int[11];
        int temp = 0;

        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        for(int k = 0; k < total; k++)
        {
            int num = Integer.parseInt(br.readLine());
            for(int i = 4; i <= num; i++) {
                dp[i] = dp[i - 3] +  dp[i-2] + dp[i-1];

            }

            System.out.println(dp[num]);
        }




    }
}
