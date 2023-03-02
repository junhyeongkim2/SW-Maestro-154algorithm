/*
 * @author Minyeong Park
 * @date 2023.02.24.
 * 문자열 분석
 * 문제 링크 : https://www.acmicpc.net/problem/10820
 */



import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = br.readLine()) != null) {
            int lower_cnt = 0, upper_cnt = 0, num_cnt = 0, space_cnt = 0;
            for (int i = 0; i < line.length(); i++) {
                char c = line.charAt(i);
                if (Character.isLowerCase(c))
                    lower_cnt++;
                else if (Character.isUpperCase(c))
                    upper_cnt++;
                else if (Character.isDigit(c))
                    num_cnt++;
                else
                    space_cnt++;
            }
            System.out.println(lower_cnt + " " + upper_cnt + " " + num_cnt + " " + space_cnt);
        }
    }
}