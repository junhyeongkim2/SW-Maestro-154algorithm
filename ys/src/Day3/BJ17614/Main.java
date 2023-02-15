package Day3.BJ17614;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
//        String s = String.valueOf(n);
        int ans = 0;

//        for (int i = 1; i <= n; i++) {
//            String s = String.valueOf(i);
//            String[] ss = s.split("");
//            for (String x: ss) {
//                if (x.equals("3")||x.equals("6")||x.equals("9")) {
//                    ans++;
//                }
//            }
//        }
        //
        Map<Integer, Integer> m = new HashMap<>();
        m.put(1,m.getOrDefault(1,0)+1);
        int[] answer = {};
        List<Integer> a = new ArrayList<>();
        a.add(1);
        a.stream().mapToInt(Integer::intValue).sorted().toArray();


        //
        for (int i = 1; i <= n; i++) {
            int temp = i;
            while (temp != 0) {
                int d = temp % 10;
                if (d == 3 || d == 6 || d == 9) {
                    ans++;
                }
                temp = temp / 10;
            }
        }


        System.out.println(ans);

    }
}
