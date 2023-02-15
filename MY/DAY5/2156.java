/*
 * @author Minyeong Park
 * @date 2023.02.12. ~ 13.
 * 포도주 시식 (Bottom-up 내가 푼 것에서 수정)
 * 원리 참고 : https://st-lab.tistory.com/135
 * 문제 링크 : https://www.acmicpc.net/problem/2156
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
            dp[2] = dp[1] + arr[2];
        }
        for (int i = 3; i <= n; i++) {
            dp[i] = Math.max(dp[i-2] + arr[i], Math.max(dp[i-1], dp[i-3] + arr[i-1] + arr[i])); // dp[n-1]과도 비교해서, 큰 값을 선택해 dp를 갱신한다.
        }

        System.out.println(dp[n]);

        // (내가 푼 것) 직접 비교하면서 최댓값 찾는 것이 좋은 게 아님
//        int max = 0;
//        for (int i = 1; i <= n; i++) {
//            if (max <= dp[i]) {
//                max = dp[i];
//            }
//        }
//
//        System.out.println(max);
    }
}