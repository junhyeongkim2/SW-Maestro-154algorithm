package DAY5;

import java.io.*;
import java.util.*;

public class BOJ_11650 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> list = new ArrayList<>();

        int total = Integer.parseInt(br.readLine());
        int arr[][] = new int[total][2];

        for(int i = 0; i < total; i++)
        {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr, (a1, a2) ->{
    if(a1[0] == a2[0]) return a1[1] - a2[1];
    else return a1[0] - a2[0];});

        for(int i = 0; i < total; i++)
        {
            System.out.println(arr[i][0]+" "+arr[i][1]);
        }

    }
}
