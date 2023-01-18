package DAY9;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2089 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        if(num == 0) sb.append(0);
        else{
            while(num != 1)
            {
                sb.append(Math.abs(num%2));
                num = (int)Math.ceil((double)num/-2);
            }
        }
        sb.append(num);
        System.out.println(sb.reverse());

    }
}
