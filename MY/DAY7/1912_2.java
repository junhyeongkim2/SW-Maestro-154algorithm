/*
 * @author Minyeong Park
 * @date 2023.02.15.
 * 연속합 (Top Down)
 * 문제 링크 : https://www.acmicpc.net/problem/1912
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] arr;
    static Integer[] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        dp = new Integer[n];
        int max = -100000000;

        arr[0] = Integer.parseInt(st.nextToken());
        dp[0] = arr[0];
        max = Math.max(max, arr[0]);

        for (int i = 1; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            find(i);
            max = Math.max(dp[i], max);
        }

        System.out.println(max);
    }

    static int find(int num) {
        if (dp[num] == null) {
            dp[num] = Math.max(find(num-1) + arr[num], arr[num]);
        }

        return dp[num];
    }
}