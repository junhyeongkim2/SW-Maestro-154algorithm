/*
 * @author Minyeong Park
 * @date 2023.02.11.
 * 이친수
 * 문제 링크 : https://www.acmicpc.net/problem/2193
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[][] arr = new long[n+1][2];
        arr[1][0] = 0;
        arr[1][1] = 1;

        for (int i = 2; i <= n; i++) {
            arr[i][0] = arr[i-1][0] + arr[i-1][1];
            arr[i][1] = arr[i-1][0];
        }

        System.out.println(arr[n][0] + arr[n][1]);
    }
}