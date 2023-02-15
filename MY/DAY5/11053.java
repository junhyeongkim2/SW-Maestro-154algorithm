/*
 * @author Minyeong Park
 * @date 2023.02.13.
 * 가장 긴 증가하는 부분 수열(Top-down)
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
    static Integer[] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        dp = new Integer[n];
        // 0 ~ n-1까지 모든 부분수열 탐색 *** (모든 인덱스에 대해 다 탐색해야 하는 것 잊지 말자)
        for (int i = 0; i < n; i++) {
            lis(i);
        }

        int max_length = dp[0];
        // 최댓값 찾기
        for (int i = 1; i < n; i++) {
            max_length = Math.max(max_length, dp[i]);
        }
        System.out.println(max_length);
    }

    static int lis(int num) {
        if (dp[num] == null) {
            dp[num] = 1;

            // num 이전의 노드들을 탐색
            for (int i = num - 1; i >= 0; i--) {
                // 이전의 노드 중 arr[num]의 값보다 작은 걸 발견했을 경우
                if (arr[i] < arr[num]) {
                    dp[num] = Math.max(dp[num], lis(i) + 1);
                }
            }
        }
        return dp[num];
    }
}