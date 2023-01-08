package DAY3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ10808 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int[] count = new int[('z' - 'a') + 1];

        for(int i = 0; i < str.length(); i++){
            count[str.charAt(i) - 'a']++;
        }

        for(int i = 0 ; i <count.length; i++){
            System.out.print(count[i] + " ");
        }
    }
}
