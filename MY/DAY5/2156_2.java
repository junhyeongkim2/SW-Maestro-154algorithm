/*
 * @author Minyeong Park
 * @date 2023.02.12. ~ 13.
 * 포도주 시식 (Top-down)
 * 원리 참고 : https://st-lab.tistory.com/135
 * 문제 링크 : https://www.acmicpc.net/problem/2156
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[] arr;
    static Integer[] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        arr = new int[n+1];
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        dp = new Integer[n+1];
        dp[0] = arr[0]; // 0번 인덱스도 초기화 해야
        dp[1] = arr[1];

        if (n >= 2) {
            dp[2] = dp[1] + arr[2];
        }
        System.out.println(find(n));
    }

    static int find(int num) {
        if (dp[num] == null) {
            dp[num] = Math.max(Math.max(find(num - 2), find(num - 3) + arr[num - 1]) + arr[num], find(num-1));
        }
        return dp[num];
    }
}