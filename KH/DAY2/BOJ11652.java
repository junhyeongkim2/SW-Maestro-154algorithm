package DAY2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class BOJ11652 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Map<Long, Integer> map = new HashMap<>();

        // counting sort 하기 위해 map 사용
        for (int i = 0; i < n; i++) {
            long thisNum = Long.parseLong(br.readLine());
            if (!map.containsKey(thisNum)) {
                map.put(thisNum, 1);
            } else {
                map.put(thisNum, map.get(thisNum) + 1);
            }
        }

        // value 값으로 내림차순 정렬 -> value 같을 때 key로 오름차순 정렬
        List<Map.Entry<Long, Integer>> mapList = new ArrayList<>(map.entrySet());
        Collections.sort(mapList, new Comparator<Map.Entry<Long, Integer>>() {
            @Override
            public int compare(Map.Entry<Long, Integer> o1, Map.Entry<Long, Integer> o2) {
                if ((long)o2.getValue() == (long)o1.getValue())
                    return Long.compare(o1.getKey(), o2.getKey());
                return o2.getValue() - o1.getValue();
            }
        });


        // print
        System.out.println(mapList.get(0).getKey());
    }
}
/*
https://www.acmicpc.net/problem/11652
*/