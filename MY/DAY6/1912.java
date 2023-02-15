/*
 * @author Minyeong Park
 * @date 2023.02.14.
 * 연속합
 * 문제 링크 : https://www.acmicpc.net/problem/1912
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] dp = new int[n];
        int max = -100000000;

        arr[0] = Integer.parseInt(st.nextToken());
        dp[0] = arr[0];
        max = Math.max(max, arr[0]);

        for (int i = 1; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            dp[i] = Math.max(dp[i-1] + arr[i], arr[i]); // 이전까지 탐색했던 값과 현재 위치의 값을 비교하여 큰 값을 저장
            max = Math.max(dp[i], max);
        }

        System.out.println(max);
    }
}