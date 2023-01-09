package DAY3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ10809 {
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        // 존재하는 문자열 저장
        int[] existAlphabet = new int['z' - 'a' + 1];
        for(int i = 0 ; i < existAlphabet.length; i++)
            existAlphabet[i] = -1;
        for(int i = 0 ; i < str.length(); i++){
            if(existAlphabet[str.charAt(i) - 'a'] == -1)
                existAlphabet[str.charAt(i) - 'a'] = i;
        }

        // print
        for(int i = 0 ; i < 26; i++){
            char thisCh = (char)('a' + i);

            if(existAlphabet[thisCh- 'a'] != -1){
                sb.append(existAlphabet[thisCh - 'a']).append(" ");
            }else
                sb.append(-1).append(" ");
        }

        System.out.println(sb.toString());
    }
}


/*
1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 */