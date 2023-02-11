/*
 * @author Minyeong Park
 * @date 2023.02.10.
 * 2×n 타일링 2 (다른 풀이 공부)
 * 참고 : https://girawhale.tistory.com/34
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
        dp[2] = 3;
        for (int i = 3; i <= n; i++) {
            dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007;
        }
        System.out.println(dp[n]);
    }
}