/*
 * @author Minyeong Park
 * @date 2023.02.24.
 * 단어 길이 재기
 * 문제 링크 : https://www.acmicpc.net/problem/2743
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        System.out.println(line.length());
    }
}