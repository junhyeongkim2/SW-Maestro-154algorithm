package DAY1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class BOJ10989 {
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        int[] list = new int[num];

        for (int i = 0; i < num; i++) {
            list[i] = Integer.parseInt(br.readLine());
        }

        // sort
        Arrays.sort(list);

        for(int i : list)
            sb.append(i).append("\n");

        System.out.println(sb.toString());
    }
}
