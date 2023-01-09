package DAY5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ11057 {
    private static final int divider = 10007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        long[][] dp = new long[num + 1][10];

        // 1의자리수 세팅
        for (int i = 0; i <= 9; i++) {
            dp[1][i] = 1;
        }

        // 나머지 자리수 세팅
        for (int i = 2; i <= num; i++) {
            for (int j = 0; j <= 9; j++) {
                long tmpSum = 0;
                for(int k = j; k <= 9; k++){
                    tmpSum += (dp[i-1][k] % divider);
                }
                dp[i][j] = (tmpSum % divider);
            }
        }

        // 총합 구하기
        long sum = 0;
        for(int i = 0; i <= 9; i++){
            sum += (dp[num][i] % divider);
        }

        System.out.println(sum % divider);


    }
}
