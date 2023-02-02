package Day2.BJ2445;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int j = 1;

        String[] anss = new String[(n-1)*2+1];
        int cnt = -1;

        while (n != 0) {
            String s = "";

            for (int i = 0; i < j; i++) {
                s += "*";
            }
            cnt++;

            for (int i = 0; i < n-1; i++) {
                s += " ";
            }

            StringBuilder sb = new StringBuilder(s);

            anss[cnt] = s + sb.reverse();
            anss[anss.length-cnt-1] = s + sb;

            j++;
            n--;
        }

        for (String x: anss) {
            System.out.println(x);
        }



    }
}
