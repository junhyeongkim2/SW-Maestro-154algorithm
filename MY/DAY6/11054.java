/*
 * @author Minyeong Park
 * @date 2023.02.14.
 * 가장 긴 바이토닉 부분 수열 (Bottom-up)
 * 문제 링크 : https://www.acmicpc.net/problem/11054
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

        // 앞에서부터 시작
        int[] dp_front = new int[n];
        for (int i = 0; i < n; i++) {
            dp_front[i] = 1;
            for (int j = 0; j < i; j++) {
                if (arr[j] < arr[i]) {
                    dp_front[i] = Math.max(dp_front[i], dp_front[j] + 1);
                }
            }
        }

        // 뒤에서부터 시작
        int[] dp_back = new int[n];
        for (int i = n-1; i >= 0; i--) {
            dp_back[i] = 1;
            for (int j = n-1; j > i; j--) {
                if (arr[j] < arr[i]) {
                    dp_back[i] = Math.max(dp_back[i], dp_back[j] + 1);
                }
            }
        }

        int max = 0;
        for (int i = 0; i < n; i++) {
            max = Math.max(max, dp_front[i] + dp_back[i] - 1);
        }
        System.out.println(max);
    }
}