package DAY9;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1212 {
    static String[] bin = {"000", "001", "010", "011", "100", "101", "110", "111"};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringBuilder sb = new StringBuilder();
        for(int i = 0 ; i < str.length(); i++)
        {
            int num = str.charAt(i) - '0';
            if(i== 0 && num < 4)
            {
                if(num < 2)
                {
                    sb.append(bin[num].substring(2));
                }
                else
                {
                    sb.append(bin[num].substring(1));
                }
            }
            else
            {
                sb.append(bin[num]);
            }

        }
        System.out.println(sb);

    }
}
