package Day1.BJ8393;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int ans = 0;

        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();

        for (int i = 1; i <= a; i++) {
            ans += i;
        }

        System.out.println(ans);
    }
}
