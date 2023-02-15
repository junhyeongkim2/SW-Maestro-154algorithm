/*
 * @author Minyeong Park
 * @date 2023.02.15.
 * 연속합 (Top Down) (다른 풀이)
 * 원리 참고 : https://st-lab.tistory.com/140
 * 문제 링크 : https://www.acmicpc.net/problem/1912
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] arr;
    static Integer[] dp;
    static int max;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        dp = new Integer[n];

        arr[0] = Integer.parseInt(st.nextToken());
        dp[0] = arr[0];
        max = arr[0];

        for (int i = 1; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // dp의 마지막 index는 n-1이므로 n-1부터 Top-down 탐색
        find(n-1);

        System.out.println(max);
    }

    static int find(int num) {
        if (dp[num] == null) {
            dp[num] = Math.max(find(num-1) + arr[num], arr[num]);
            max = Math.max(dp[num], max);
        }

        return dp[num];
    }
}