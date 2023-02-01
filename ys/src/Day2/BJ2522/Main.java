package Day2.BJ2522;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = n;
        String[] ans = new String[2*n-1];
        int stars = 1;

        while (n!=0) {
            String s = "";
            for (int i = 0; i < m-stars; i++) {
                s += " ";
            }
            for (int i = 0; i < stars; i++) {
                s += "*";
            }

            ans[stars - 1] = s;
            ans[ans.length - stars] = s;

            stars++;
            n--;
        }

        for (String x :
                ans) {
            System.out.println(x);
        }
    }
}
