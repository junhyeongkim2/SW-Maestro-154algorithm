/*
 * @author Minyeong Park
 * @date 2023.02.13.
 * 가장 긴 증가하는 부분 수열 (Bottom up)
 * 원리 참고 출처 : https://st-lab.tistory.com/137
 * 문제 링크 : https://www.acmicpc.net/problem/11053
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[] arr;
    static int[] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        dp = new int[n];
        // 0 ~ n-1까지 모든 부분수열 탐색 *** (모든 인덱스에 대해 다 탐색해야 하는 것 잊지 말자)
        for (int i = 0; i < n; i++) {
            dp[i] = 1; // 먼저 1로 초기화해줘야 함!
            for (int j = 0; j < i; j++) {
                if (arr[j] < arr[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        int max_length = dp[0];
        // 최댓값 찾기
        for (int i = 1; i < n; i++) {
            max_length = Math.max(max_length, dp[i]);
        }
        System.out.println(max_length);
    }
}