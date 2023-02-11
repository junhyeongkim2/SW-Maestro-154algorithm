/*
 * @author Minyeong Park
 * @date 2023.02.10. ~ 11.
 * 쉬운 계단 수
 * 문제 링크 : https://www.acmicpc.net/problem/10844
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] dp = new int[101][10]; // n은 1 ~ 100, 0 ~ 9까지 올 수 있으므로
        //    n = 1 2 3 4 일 때
        // 0      0 <- n=1일 때 0이 맨 뒤에 오는 개수
        // 1      1 <- n=1일 때 1이 맨 뒤에 오는 개수
        // 2      1
        // 3      1
        dp[1][0] = 0;
        for (int i = 1; i <= 9; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i <= n; i++) {
            dp[i][0] = dp[i-1][1];
            dp[i][9] = dp[i-1][8];
            for (int j = 1; j <= 8; j++) {
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000; // 더하면 값이 너무 커지니까 여기에서도 한번 10억으로 나눠줌
            }
        }

        long count = 0;
        for (int i = 0; i <= 9; i++) {
            count += dp[n][i] ;
        }
        System.out.println(count % 1000000000); // 더하면 값이 너무 커지니까 여기에서도 한번 10억으로 나눠줌
    }
}