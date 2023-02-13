/*
 * @author Minyeong Park
 * @date 2023.02.12.
 * 스티커 // 조금 더 효율적으로 수정함
 * 문제 링크 : https://www.acmicpc.net/problem/9465
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int[][] arr = new int[n][2];
            int[][] dp = new int[n][2];
            for (int x = 0; x < 2; x++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int y = 0; y < n; y++) {
                    arr[y][x] = Integer.parseInt(st.nextToken());
                }
            }

            dp[0][0] = arr[0][0];
            dp[0][1] = arr[0][1];

            if (n >= 2) {
                dp[1][0] = arr[1][0] + dp[0][1];
                dp[1][1] = arr[1][1] + dp[0][0];
            }
            for (int a = 2; a < n; a++) {
                dp[a][0] = arr[a][0] + Math.max(dp[a-1][1], dp[a-2][1]);
                dp[a][1] = arr[a][1] + Math.max(dp[a-1][0], dp[a-2][0]);
            }

            System.out.println(Math.max(dp[n-1][0], dp[n-1][1]));
        }
    }
}