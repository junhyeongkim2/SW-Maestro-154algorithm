/*
 * @author Minyeong Park
 * @date 2023.02.11.
 * 오르막 수
 * 문제 링크 : https://www.acmicpc.net/problem/11057
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[1001][10];
        for (int i = 0; i < 10; i++) {
            arr[1][i] = 1;
        }
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < 10; j++) {
                for (int k = 0; k <= j; k++) {
                    arr[i][j] = (arr[i][j] + arr[i-1][k]) % 10007;
                }
            }
        }

        int result = 0;
        for (int i = 0; i < 10; i++) {
            result = (result + arr[n][i]) % 10007;
        }
        System.out.println(result % 10007);
    }
}