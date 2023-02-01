package Day2.BJ2442;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String s = "*";

        while (n!=0) {
            for (int i = 0; i < n-1; i++) {
                System.out.printf(" ");
            }

            System.out.printf(s);
            s += "**";
            System.out.println();

            n--;
        }
    }
}

