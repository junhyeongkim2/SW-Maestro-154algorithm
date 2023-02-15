package Day3.BJ17614;

import java.util.*;

public class Main2 {
    static int[] ans = new int[7];
    static int[] hat = new int[9];

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 9; i++) {
            hat[i] = sc.nextInt();
        }

        combination(0,0);

    }


    static void combination(int start, int count){

        if (count == 7) {
            int total = 0;

            for (int i = 0; i < 7; i++) {
                total+=ans[i];
            }

            if (total == 100) {
                for (int x : ans) {
                    System.out.println(x);
                }
            }

            return;
        }

        for (int i = start; i < 9; i++) {
            ans[count] = hat[i];
            combination(i+1,count+1);
        }


    }
}
