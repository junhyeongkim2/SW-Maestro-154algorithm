/*
 * @author Minyeong Park
 * @date 2023.02.13.
 * 가장 큰 증가 부분 수열 (Bottom up)
 * 반례 참고 : https://www.acmicpc.net/board/view/87941
 * 문제 링크 : https://www.acmicpc.net/problem/11055
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int[] dp = new int[n];
        dp[0] = arr[0];

        for (int i = 1; i < n; i++) {
            dp[i] = arr[i]; // i번째 보다 작은 인덱스를 탐색할 때 먼저 dp[i]를 초기화해주는 것 잊지 말자!
            for (int j = 0; j < i; j++) {
                if (arr[j] < arr[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + arr[i]);
                }
            }
        }

        int max = 0;
        for (int sum : dp) {
            max = Math.max(sum, max);
        }

        System.out.println(max);
    }
}