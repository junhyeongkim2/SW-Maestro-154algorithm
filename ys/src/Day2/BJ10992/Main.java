package Day2.BJ10992;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int total = n;

        while (n != 0) {
            String s = "";

            for (int i = 0; i < n-1; i++) {
                s += " ";
            }

            if (n == 1) {
                for (int i = 0; i < 2*total-1; i++) {
                    s += "*";
                }
            } else {
                for (int i = 0; i < 2*(total-n)+1; i++) {
                    if (i == 0||i==2*(total-n)) {
                        s += "*";
                    } else s += " ";
                }
            }

            System.out.println(s);
            n--;
        }

    }
}
