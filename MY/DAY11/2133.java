/*
 * @author Minyeong Park
 * @date 2023.02.26.
 * 타일 채우기
 * 원리 참고 : https://velog.io/@matcha_/%EB%B0%B1%EC%A4%80-2133-%ED%83%80%EC%9D%BC-%EC%B1%84%EC%9A%B0%EA%B8%B0-C-DP
 * 문제 링크 : https://www.acmicpc.net/problem/2133
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[31];
        dp[0] = 1;
        dp[2] = 3;
        for (int i = 4; i <= n; i++) {
            dp[i] = dp[i-2] * dp[2];
            if (i % 2 == 0) {
                for (int j = i-4; j >= 0; j--) {
                    dp[i] += dp[j] * 2;
                }
            }
        }
        System.out.println(dp[n]);
    }
}