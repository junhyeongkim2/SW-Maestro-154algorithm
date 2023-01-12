package DAY4;

import java.io.*;
import java.util.*;


public class BOJ_2193 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        long[] dp = new long[num+1]; // 0~9 까지 경우의 수
        dp[0] = 0;
        dp[1] = 1;

        for(int i = 2; i<= num; i++){
            dp[i] = dp[i-2] + dp[i-1];
        }
        System.out.println(dp[num]);


    }
}
