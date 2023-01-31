package Day1.BJ1924;

import java.util.Scanner;

public class Main {

    static String solution1(String a, String b) {

        String[] week = new String[]{"SUN","MON","TUE","WED","THU","FRI","SAT"};
        String smallM = "(4|6|9|11)";

        int day = 0;
        int x = Integer.parseInt(a);
        int y = Integer.parseInt(b);

        if (x == 1) {
            return week[y % 7];
        }

        for (int i = 1; i <= x - 1; i++) {
            String temp = String.valueOf(i);
            if (i == 2) {
                day +=  28;
            } else if (temp.matches(smallM)) {
                day +=  30;
            } else day += 31;
        }

        day += y;

        return week[day % 7];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] s = sc.nextLine().split(" ");

        System.out.println(solution1(s[0],s[1]));

    }
}
