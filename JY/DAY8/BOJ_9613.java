package DAY8;

import java.io.IOException;
import java.io.InputStreamReader;

import java.io.*;
import java.util.*;

public class BOJ_9613 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = Integer.parseInt(br.readLine());
        StringTokenizer st;


        for(int i = 0; i < total; i++){
            String[] input = br.readLine().split(" ");
            int num = Integer.parseInt(input[0]);
            int[] inputs = new int[num];
            long res = 0;
            for(int n = 1; n <=  num; n++)
            {
                inputs[n-1] = Integer.parseInt(input[n]);


            }

            for(int j = 0; j < inputs.length-1; j++)
            {
                for(int k = j+1; k < inputs.length; k++)
                {

                    res = res + gcd(Math.max(inputs[j], inputs[k]), Math.min(inputs[j], inputs[k]));
                }
            }
            System.out.println(res);

        }


    }
    public static int gcd(int a, int b)
    {
        if(b <= 0)
        {
            return a;
        }
        return gcd(b, a%b);
    }



}
