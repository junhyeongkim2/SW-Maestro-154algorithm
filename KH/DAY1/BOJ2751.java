package DAY1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ2751 {
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> list = new ArrayList<>();

        // set input
        int num = Integer.parseInt(st.nextToken());
        for(int i = 0 ; i < num; i++){
            st = new StringTokenizer(br.readLine());
            list.add(Integer.parseInt(st.nextToken()));
        }

        // sort
        Collections.sort(list);

        // print
        for(int i : list)
            sb.append(i).append("\n");
        System.out.println(sb.toString());
    }
}

/*
https://www.acmicpc.net/problem/2751

Collections.sort() -> 시간 복잡도 만족
but, 매번 println 해주면 시간 초과 -> StringBuilder 사용
 */