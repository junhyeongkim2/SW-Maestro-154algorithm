package Day2.BJ2446;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int total = 2*n-1;
        String[] ans = new String[total];
        int idx = 0;

        while (n != 0) {
            int stars = 2*n-1;
            String s = "";

            for (int i = 0; i < idx; i++) {
                s += " ";
            }
            for (int i = 0; i < stars; i++) {
                s += "*";
            }

            ans[idx] = s;
            ans[total - idx - 1] = s;

            idx++;
            n--;
        }

        for (String x :
                ans) {
            System.out.println(x);
        }
    }
}
