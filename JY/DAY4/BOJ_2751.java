package DAY4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class BOJ_2751 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < total; i++ )
        {
            list.add(Integer.parseInt(br.readLine()));
        }
        Collections.sort(list);
        for(int k : list){
            sb.append(k).append("\n");
        }
        System.out.println(sb);

    }
}
