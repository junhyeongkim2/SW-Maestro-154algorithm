/*
 * @author Minyeong Park
 * @date 2023.02.12. ~ 13.
 * 계단 오르기 (Bottom-up)
 * 원리 참고 출처 : https://st-lab.tistory.com/132
 * 문제 링크 : https://www.acmicpc.net/problem/2579
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n+1];
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int[] dp = new int[n+1];
        dp[1] = arr[1];
        if (n >= 2) {
            dp[2] = arr[1] + arr[2];
        }
        for (int i = 3; i <= n; i++) {
            dp[i] = Math.max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i]);
        }

        System.out.println(dp[n]);
    }
}