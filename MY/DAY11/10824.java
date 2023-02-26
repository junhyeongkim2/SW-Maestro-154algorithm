/*
 * @author Minyeong Park
 * @date 2023.02.26.
 * 네 수
 * 문제 링크 : https://www.acmicpc.net/problem/10824
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long first = Long.parseLong(st.nextToken() + st.nextToken());
        long second = Long.parseLong(st.nextToken() + st.nextToken());
        System.out.println(first + second);
    }
}