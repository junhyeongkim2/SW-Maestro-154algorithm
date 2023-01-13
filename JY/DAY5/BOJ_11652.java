package DAY5;

import java.io.*;
import java.util.*;
public class BOJ_11652 {
    public static void main(String[] arg) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = Integer.parseInt(br.readLine());
        Long maxIndex = (long)0;
        int max = 0;
        HashMap<Long, Integer> map = new HashMap<Long, Integer>();
        for(int i = 0; i < total; i++) {
            Long index = Long.parseLong(br.readLine());
            map.put(index, map.getOrDefault(index, 0) + 1);
        }

        for(Map.Entry<Long, Integer> entry : map.entrySet())
        {
            if(max < entry.getValue()) {
                max = entry.getValue();
                maxIndex = entry.getKey();
            }
            else if(max == entry.getValue())
            {
                maxIndex = Math.min(maxIndex, entry.getKey());
            }
        }
        System.out.println(maxIndex);


    }
}
