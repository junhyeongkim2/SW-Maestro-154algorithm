package DAY4;

import java.io.*;
import java.util.*;


public class BOJ_2193 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        int[] dp = new int[num+1]; // 0~9 까지 경우의 수
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 1;
        dp[3] = 2;
        dp[4] = 5;

        for(int i = 5; i<= num; i++){
            dp[i] = dp[i-2] + dp[i-1];
        }
        System.out.println(dp[num]);


    }
}
