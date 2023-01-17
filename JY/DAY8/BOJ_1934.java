package DAY8;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1934 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int total = Integer.parseInt(br.readLine());

        for(int i = 0; i < total; i++)
        {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if(b > a){
                int temp = a;
                a = b;
                b = temp;
            }
            int d = gcd(a, b);
            System.out.println((a*b)/d);


        }

    }
    public static int gcd(int a, int b)
    {
        if(b <= 0) return a;
        return gcd(b, a%b);
    }

}
