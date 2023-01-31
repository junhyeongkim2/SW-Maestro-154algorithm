package Day1.BJ10818;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());
        String[] s = sc.nextLine().split(" ");

        int min = Integer.parseInt(s[0]);
        int max = Integer.parseInt(s[0]);

        for (int i = 0; i < n; i++) {
            int temp = Integer.parseInt(s[i]);
            if (temp > max) {
                max = temp;
            }
            if (temp < min) {
                min = temp;
            }
        }

        System.out.println(min + " " + max);
    }
}
