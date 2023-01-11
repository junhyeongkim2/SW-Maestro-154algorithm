package DAY2;

import java.io.InputStreamReader;

import java.io.*;
import java.util.*;

public class BOJ_11726 {
    public static void main(String[] arg) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = Integer.parseInt(br.readLine());
        int dp[] = new int[total + 1];
        dp[1] = 1;
        dp[2] = 2;

        for(int i =3; i <= total; i++)
        {
            dp[i] = (dp[i-1] + dp[i-2]) % 10007;

        }
        System.out.println(dp[total]);


    }

}
