package DAY4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BOJ9095 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        List<Integer> targetList = new ArrayList<>();
        for (int i = 0; i < num; i++) {
            targetList.add(Integer.parseInt(br.readLine()));
        }

        int maxNum = Collections.max(targetList);
        int[] dp = new int[(maxNum > 3) ? maxNum + 1 : 3 + 1];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        for (int i = 4; i <= maxNum; i++) {
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1];
        }

        for (int target : targetList) {
            System.out.println(dp[target]);
        }
    }
}
