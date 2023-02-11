/*
 * @author Minyeong Park
 * @date 2023.02.10.
 * 2×n 타일링 2 (내가 푼 것인데 점화식이.. 값은 잘 나오긴 하지만 원리에서 도출한 것은 아니다..)
 * 문제 링크 : https://www.acmicpc.net/problem/11727
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] dp = new long[1001];
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                dp[i] = (dp[i-1] * 2 + 1) % 10007;
            } else {
                dp[i] = (dp[i-1] * 2 - 1) % 10007;
            }
        }
        System.out.println(dp[n]);
    }
}