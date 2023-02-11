/*
 * @author Minyeong Park
 * @date 2023.02.11.
 * 이친수 (다른 풀이 공부)
 * 출처 : 이전에 풀었던 코드 다시 참고
 * 원리 참고 : https://odysseyj.tistory.com/25
 * // 나는 개수가 증가하는 원리를 따져서 진행했는데... 더 간단한 원리로 가능하다.
 * 문제 링크 : https://www.acmicpc.net/problem/2193
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] arr = new long[n+1];
        arr[1] = 1;

        for (int i = 2; i <= n; i++) {
            arr[i] = arr[i-1] + arr[i-2];
        }

        System.out.println(arr[n]);
    }
}