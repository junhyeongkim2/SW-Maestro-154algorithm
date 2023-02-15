/*
 * @author Minyeong Park
 * @date 2023.02.14.
 * 가장 긴 감소하는 부분 수열 (Top Down)
 * 문제 링크 : https://www.acmicpc.net/problem/11722
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
        dp[0] = 1;
        for (int i = 1; i < n; i++) {
            dp[i] = lds(i);
        }

        int max_len = 0;
        for (int len : dp) {
            max_len = Math.max(max_len, len);
        }
        System.out.println(max_len);
    }

    static int lds(int num) {
        if (dp[num] == null) {
            dp[num] = 1;
            for (int j = 0; j < num; j++) {
                if (arr[j] > arr[num]) {
                    dp[num] = Math.max(dp[num], dp[j] + 1);
                }
            }
        }
        return dp[num];
    }
}