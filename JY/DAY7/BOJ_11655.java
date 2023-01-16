package DAY7;

import javax.swing.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_11655 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++)
        {
            if(s.charAt(i) >= 'A' && s.charAt(i) <='Z')
            {
                if(s.charAt(i) < 'N') sb.append((char)(s.charAt(i) + 13));
                else sb.append((char)(s.charAt(i) - 13));
            }
            else if(s.charAt(i) >= 'a' && s.charAt(i) <= 'z')
            {
                if(s.charAt(i) < 'n') sb.append((char)(s.charAt(i) + 13));
                else sb.append((char)(s.charAt(i) - 13));
            }
            else
            {
                sb.append(s.charAt(i));
            }
        }
        System.out.println(sb);
    }
}
