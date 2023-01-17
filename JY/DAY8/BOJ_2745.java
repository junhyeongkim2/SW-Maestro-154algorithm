package DAY8;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_2745 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String str = st.nextToken();
        int ex = Integer.parseInt(st.nextToken());

        long res = 0;
        for(int i = 0; i < str.length(); i++)
        {
            if(str.charAt(i) >= 'A' && str.charAt(i) <= 'Z')
            {
                res = res *ex + (str.charAt(i) - 55);
            }
            else{
                res = res* ex + (str.charAt(i) - '0');
            }
        }
        System.out.println(res);

    }
}
