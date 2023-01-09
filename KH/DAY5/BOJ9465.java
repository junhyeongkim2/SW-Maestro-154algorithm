package DAY5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ9465 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for (int i = 0; i < testCase; i++) {
            // sticker 배열 세팅
            int n = Integer.parseInt(br.readLine());
            int[][] sticker = new int[2][n];
            int[][] dp = new int[2][n];
            for (int j = 0; j < 2; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int k = 0; k < n; k++) {
                    sticker[j][k] = Integer.parseInt(st.nextToken());
                }
            }

            // initialize
            dp[0][0] = sticker[0][0];
            dp[1][0] = sticker[1][0];
            if (n >= 2) {
                dp[0][1] = dp[1][0] + sticker[0][1];
                dp[1][1] = dp[0][0] + sticker[1][1];
            }

            // calculate
            for (int j = 2; j < n; j++) {
                dp[0][j] = Math.max(dp[1][j-1], dp[1][j-2]) + sticker[0][j];
                dp[1][j] = Math.max(dp[0][j-1], dp[0][j-2]) + sticker[1][j];
            }

            System.out.println(Math.max(dp[0][n-1], dp[1][n-1]));
        }
    }
}
