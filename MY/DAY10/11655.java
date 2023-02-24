/*
 * @author Minyeong Park
 * @date 2023.02.24.
 * ROT13
 * 문제 링크 : https://www.acmicpc.net/problem/11655
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c == ' ' || Character.isDigit(c)) {
                System.out.print(c);
            } else if (Character.isUpperCase(c)) {
                char ch = (char) (c + 13);
                if (ch > 'Z') {
                    ch = (char) (ch - 26);
                }
                System.out.print(ch);
            } else if (Character.isLowerCase(c)) {
                char ch = (char) (c + 13);
                if (ch > 'z') {
                    ch = (char) (ch - 26);
                }
                System.out.print(ch);
            }
        }
    }
}