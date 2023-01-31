package Day1.BJ11720;


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int num = Integer.parseInt(sc.nextLine());
        String input = sc.nextLine();

        int ans = 0;

        for (int i = 0; i < num; i++) {
            ans += Integer.parseInt(String.valueOf(input.charAt(i)));
        }

        System.out.println(ans);

    }
}

