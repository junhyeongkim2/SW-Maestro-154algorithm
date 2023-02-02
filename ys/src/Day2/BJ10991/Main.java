package Day2.BJ10991;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = n;

        while (n != 0) {
            String s = "";

            for (int i = 0; i < n-1; i++) {
                s += " ";
            }

            for (int i = 0; i < 2*(m-n+1)-1; i++) {
                if (i % 2 == 0) {
                    s += "*";
                } else s += " ";
            }

            System.out.println(s);
            n--;
        }
    }
}
