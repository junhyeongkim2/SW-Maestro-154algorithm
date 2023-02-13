/*
 * @author Minyeong Park
 * @date 2023.02.12. ~ 13.
 * 계단 오르기 (Top-Down)
 * 원리 참고 출처 : https://st-lab.tistory.com/132
 * 문제 링크 : https://www.acmicpc.net/problem/2579
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int n;
    static int[] arr;
    static Integer[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n+1];
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        dp = new Integer[n+1];
        dp[0] = arr[0]; // 디폴트 값이 null이므로, 0으로 초기화 해야 함!
        dp[1] = arr[1];
        if (n >= 2) {
            dp[2] = arr[1] + arr[2];
        }

        System.out.println(find(n));
    }

    static int find(int num) {
        if (dp[num] == null) { // 아직 탐색하지 않은 N번째 계단일 경우
            dp[num] = Math.max(find(num-2), find(num-3) + arr[num-1]) + arr[num];
        }
        return dp[num];
    }
}