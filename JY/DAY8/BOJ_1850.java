package DAY8;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1850 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        if(b > a)
        {
            long temp = a;
            a = b;
            b = temp;
        }
        long d = gcd(a, b);
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < d; i++){
            sb.append("1");
        }
        System.out.println(sb);



    }
    public static long gcd(long a, long b){
        if(b <= 0) return a;
        return gcd(b, a%b);
    }
}
