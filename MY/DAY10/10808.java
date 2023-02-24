/*
 * @author Minyeong Park
 * @date 2023.02.23.
 * 알파벳 개수
 * 문제 링크 : https://www.acmicpc.net/problem/10808
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int[] arr = new int[26];

        for (int i = 0; i < s.length(); i++) {
            arr[s.charAt(i) - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}