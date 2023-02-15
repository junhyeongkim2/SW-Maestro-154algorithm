package Day3.BJ3040;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] dwarf = new int[9];

        for (int i = 0; i < 9; i++) {
            dwarf[i] = sc.nextInt();
        }

        int sum = Arrays.stream(dwarf).sum();

        int a = 0;
        int b = 0;


        for (int i = 0; i < 9; i++) {
            for (int j = i+1; j < 9; j++) {
                if (sum - (dwarf[i] + dwarf[j]) == 100) {
                    a=i;
                    b=j;

//                    System.out.printf("%d %d\n",a,b);
                    break;
                }
            }
            if (a != b) {
                break;
            }
        }

        for (int i = 0; i < 9; i++) {
            if (i != a && i != b) {
                System.out.println(dwarf[i]);
            }
        }
    }

}
