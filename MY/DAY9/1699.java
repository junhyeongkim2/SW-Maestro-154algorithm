/*
 * @author Minyeong Park
 * @date 2023.02.23.
 * 제곱수의 합
 * 원리 및 반례 참고 : https://maivve.tistory.com/199, https://www.acmicpc.net/board/view/108759, https://www.acmicpc.net/board/view/99588
 * 문제 링크 : https://www.acmicpc.net/problem/1699
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] dp = new int[100001];
        for (int i = 1; i <= Math.sqrt(100000); i++) {
            dp[i * i] = 1;
        }

        int max_sq_num = 0;
        for (int i = 1; i <= n; i++) {
            if (dp[i] == 1) {
                max_sq_num = i;
            } else {
                dp[i] = dp[i - max_sq_num] + 1;
                for (int j = 1; j < Math.sqrt(max_sq_num); j++) {
                    dp[i] = Math.min(dp[i], dp[i - j*j] + 1);
                }
            }
        }

        System.out.println(dp[n]);
    }
}