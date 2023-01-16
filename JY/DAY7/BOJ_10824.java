package DAY7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class BOJ_10824 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        String ab = st.nextToken() + st.nextToken();
        String cd = st.nextToken() + st.nextToken();

        System.out.println(Long.parseLong(ab)+Long.parseLong(cd));
    }
}
