package 복기.도미노.bj17135;

import java.util.*;

public class Solution {
    int[] arcpos;
    boolean[] visited;
    int answer = 0;
    List<int[]> ar = new ArrayList<>();

    public void attackRange(int total){
        for(int i = 1; i<=total;i++){
            int param = -i+1;

            for(int j = param;j<i;j++){
                int h = i-Math.abs(j);
                ar.add(new int[]{h,j});
            }
        }

//        ar.stream().forEach(x->System.out.println(Arrays.toString(x)));

    }

    public void kill (int[] arcpos, int[][]map, int n, int m){
        int cnt = 0;
        int[][] mapTemp = new int[n][m];
        for (int i = 0; i < n; i++) {
            mapTemp[i] = map[i].clone();
        }

        for (int i = n-1; i > -1; i--) {
            List<int[]> hunted = new ArrayList<>();
            for (int j = 0; j < m; j++) {
                // 궁수가 있으면
                if(arcpos[j]==1){
                    // 궁수의 범위에 몬스터 있으면
                        for(int[] target : ar){
                            // 몬스터 킬, 턴 끝남
                            try{
                                if (mapTemp[i - target[0] + 1][j + target[1]] == 1) {
                                    hunted.add(new int[]{i - target[0] + 1,j + target[1]});
//                                    mapTemp[i - target[0] + 1][j + target[1]] += 1;
                                    break;

                                }
                            } catch (Exception e ) {
                                continue;
                            }
                        }

                }

            }

            for(int[] a : hunted){
                mapTemp[a[0]][a[1]] -= 2;
            }

//            System.out.println(n-i);
//            for (int[] a: mapTemp
//                 ) {
//                System.out.println(Arrays.toString(a));
//            }
//            System.out.println("---------------------------------");
//            System.out.println(Arrays.toString(arcpos));
//            System.out.println("=================================");

        }

        for(int[] x : mapTemp){
            for(int y : x){
                if(y<0) cnt++;
            }
        }

        answer = Math.max(answer, cnt);

//        System.out.println("######################################");
//        System.out.print("answer : ");
//        System.out.println(answer);
//        System.out.println("######################################");
    }

    public void positions (int m, int start, int pick, int[][]map, int n){

        if(pick==0){
            kill(arcpos, map, n, m);
            return;
        }

        for (int i = start; i < m; i++) {
            if(!visited[i]){
                visited[i] = true;
                arcpos[i] = 1;
                positions(m, i + 1, pick - 1, map, n);
                visited[i] = false;
                arcpos[i] = 0;
            }

        }
    }

    public int solution(int n, int m, int d, int[][]map){

        arcpos = new int[m];
        visited = new boolean[m];

        attackRange(d);
//        ar.stream().forEach(x -> System.out.println(Arrays.toString(x)));
        positions(m,0,3, map, n);


        return answer;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int d = sc.nextInt();

        int[][] map = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                map[i][j] = sc.nextInt();
            }
        }

        int test = new Solution().solution(n, m, d, map);
        System.out.println(test);
    }
}
