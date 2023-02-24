/*
 * @author Minyeong Park
 * @date 2023.02.23.
 * 제곱수의 합 (다른 분 풀이)
 * 출처 : https://www.acmicpc.net/board/view/99588
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

        for (int i = 1; i <= n; i++) {
            // 최소가 되는 제곱수 = n의 이전 수들 중 제곱수 + n - 제곱수의 최수항 개수
            for (int j = 1; j*j < i; j++) {
                if (dp[i] > dp[i - (j * j)] + 1) {
                    dp[i] = dp[i - (j * j)] + 1;
                }
            }
        }

        System.out.println(dp[n]);
    }
}