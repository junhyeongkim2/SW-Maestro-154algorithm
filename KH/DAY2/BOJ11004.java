package DAY2;

import java.io.*;
import java.util.*;

public class BOJ11004 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input setting
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] num = new int[n];

        st = new StringTokenizer(br.readLine());
        for(int i = 0 ; i < n; i++){
            num[i] = Integer.parseInt(st.nextToken());
        }

        // sorting
        Arrays.sort(num);

        // print
        System.out.println(num[k-1]);

    }
}
