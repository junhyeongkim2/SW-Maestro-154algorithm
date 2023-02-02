package Day2.BJ2441;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = n;

        while (n!=0) {

            for (int i = n; i > 0; i--) {
                System.out.printf("*");
            }

            n--;
            if (n == 0) {
                break;
            }
            System.out.println();
            for (int i = 0; i < m-n; i++) {
                System.out.printf(" ");
            }
        }
    }
}
