package DAY3;

import java.io.*;
import java.util.*;

public class BOJ_11057 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        long[][] dp = new long[num+1][10]; // 0~9 까지 경우의 수
        long res = 0;

        for(int i =0 ; i < 10; i++)
        {
            dp[1][i] = 1;
        }
        for(int i = 1; i <= num; i++)
        {
            for(int j = 0; j <= 9; j++)
            {
                if(j == 0) dp[i][j] = 0;
                else {
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1])%10007;
                }
                if(i == num) res += dp[i][j];
            }

        }
        System.out.println(res%10007);

    }
}
