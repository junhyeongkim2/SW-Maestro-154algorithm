package Day1.BJ11721;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();

        for (int j = 0; j < s.length()/10+1; j++) {
            if (j == s.length()/10) {
                System.out.println(s.substring(j*10));
            } else System.out.println(s.substring(j*10,j*10+10));

        }

    }
}
