/*
 * @author Minyeong Park
 * @date 2023.02.14.
 * 가장 긴 바이토닉 부분 수열 (Top Down)
 * 문제 링크 : https://www.acmicpc.net/problem/11054
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[] arr;
    static Integer[] dp_front, dp_back;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 앞에서부터 시작
        dp_front = new Integer[n];
        for (int i = 0; i < n; i++) {
            front(i);
        }

        // 뒤에서부터 시작
        dp_back = new Integer[n];
        for (int i = n-1; i >= 0; i--) {
            back(i);
        }

        int max = 0;
        for (int i = 0; i < n; i++) {
            max = Math.max(max, dp_front[i] + dp_back[i] - 1);
        }
        System.out.println(max);
    }

    static int front(int num) {
        if (dp_front[num] == null) {
            dp_front[num] = 1;
            for (int j = 0; j < num; j++) {
                if (arr[j] < arr[num]) {
                    dp_front[num] = Math.max(dp_front[num], front(j) + 1);
                }
            }
        }
        return dp_front[num];
    }

    static int back(int num) {
        if (dp_back[num] == null) {
            dp_back[num] = 1;
            for (int j = n-1; j > num; j--) {
                if (arr[j] < arr[num]) {
                    dp_back[num] = Math.max(dp_back[num], back(j) + 1);
                }
            }
        }
        return dp_back[num];
    }
}