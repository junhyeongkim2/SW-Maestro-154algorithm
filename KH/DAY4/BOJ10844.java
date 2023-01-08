package DAY4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ10844 {
    private static final int divider = 1000000000;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        long[][] dp = new long[num+1][10];

        // 1의자리 수 계단수 개수 저장
        for(int i = 1; i <= 9; i++){
            dp[1][i] = 1;
        }

        // 10의자리 수부터 계단수 개수 계산
        for(int i = 2; i <=num; i++){
            for(int j = 0 ; j <= 9; j++){
                if(j == 0)
                    dp[i][j] = dp[i-1][1] % divider;
                else if(j== 9)
                    dp[i][j] = dp[i-1][8] % divider;
                else
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] % divider;
            }
        }

        int sum = 0;
        for(long target : dp[num]){
            sum += (target % divider);
        }

        System.out.println(sum);
    }
}

/*
1 -> 10 12 -> 101 121 123
2 -> 21 23 -> 210 212 232 234
3 -> 32 34 -> 321 323 343 345
4 -> 43 45
5
6
7 -> 76 78 -> 765 767 787 789
8 -> 87 89 -> 876 878 898
9 -> 98    -> 987 989

(0, 1) -> (1, 1) -> (1, 2) -> (3, 2) ->

9 => 17(8*2 + 1) => 32(15*2 + 1+ 1) =>

 */