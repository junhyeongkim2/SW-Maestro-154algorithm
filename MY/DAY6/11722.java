/*
 * @author Minyeong Park
 * @date 2023.02.14.
 * 가장 긴 감소하는 부분 수열 (Bottom up)
 * 추가 내용 참고 : https://st-lab.tistory.com/137
 * 문제 링크 : https://www.acmicpc.net/problem/11722
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
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[n];
        dp[0] = 1;
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (arr[j] > arr[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1); // 그냥 값만 크다고 해서 비교해줘도 되고
                }

//                // j번째 원소가 i번째 원소보다 작으면서 i번째 dp가 j번째 dp+1 값보다 작은 경우
//                if (arr[j] > arr[i] && dp[i] < dp[j] + 1) { //s if문에서 dp값이 더 작은지도 추가로 비교해줘도 좋음
//                    dp[i] = dp[j] + 1;
//                }
            }
        }

        int max_len = 0;
        for (int len : dp) {
            max_len = Math.max(max_len, len);
        }
        System.out.println(max_len);
    }
}