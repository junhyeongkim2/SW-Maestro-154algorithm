package DAY8;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_11005 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long num = Long.parseLong(st.nextToken());
        int ex = Integer.parseInt(st.nextToken());
        List<Character> list = new ArrayList<>();
        while(num > 0)
        {
            if(num % ex < 10)
            {
                list.add((char)(num%ex + '0' ));
            }
            else{
                list.add((char)((num%ex - 10) + 'A'));
            }
            num = num / ex;
        }
        for(int i = list.size()-1; i >= 0 ; i--)
        {
            System.out.print(list.get(i));
        }

    }




}
