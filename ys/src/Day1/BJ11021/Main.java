package Day1.BJ11021;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int nextInt = sc.nextInt();
        sc.nextLine(); //nextInt는 개행문자 전까지만

        for (int i = 0; i < nextInt; i++) {
            String[] split = sc.nextLine().split(" ");
            System.out.printf("Case #%d: %d\n",i+1,Integer.parseInt(split[0])+Integer.parseInt(split[1]));
        }

    }
}

