package 프로그래머스_고득점_kit.DP.등굣길;

import java.util.*;

//시간초과(효율성 TC 1,5,8) -> 문제에서 "오른쪽과 아래로만 움직이는" 조건이 있음. dfs로 접근해보자.
public class Solution_bfs {

    public void bfs(int[][] map, boolean[][] visited, boolean[][] isAdd){

        int[] dx = new int[]{1,0,-1,0};
        int[] dy = new int[]{0,1,0,-1};

        Queue<int[]> q = new LinkedList<>();

        q.add(new int[]{0,0});
        map[0][0]++;
        visited[0][0] = true;
        isAdd[0][0] = true;


        while(!q.isEmpty()){
            int[] temp = q.poll();
            int y = temp[0];
            int x = temp[1];

            if(x==map[0].length-1&&y==map.length-1){
                return;
            }

            for(int i = 0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(ny<0||nx<0||ny>map.length-1||nx>map[0].length-1) continue;

                if(!visited[ny][nx]){
                    // System.out.printf("Before (%d,%d) -> (%d,%d)\n",x,y,nx,ny);
                    // for(int[] k : map){
                    //     System.out.println(Arrays.toString(k));
                    // }
                    map[ny][nx] = (map[ny][nx] + map[y][x])%1000000007;
                    if(!isAdd[ny][nx]){
                        q.add(new int[]{ny,nx});
                        isAdd[ny][nx] = true;
                    }
                    // System.out.printf("After (%d,%d) -> (%d,%d)\n",x,y,nx,ny);
                    // for(int[] k : map){
                    //     System.out.println(Arrays.toString(k));
                    // }
                    // System.out.printf("\n");
                }
            }
            visited[y][x] = true;

        }


    }


    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;

        int[][] map = new int[n][m];
        boolean[][] visited = new boolean[n][m];
        boolean[][] isAdd = new boolean[n][m];

        for(int[] p : puddles){
            visited[p[1]-1][p[0]-1] = true;
        }

        bfs(map, visited, isAdd);

        // for(int[] y : map){
        //     System.out.println(Arrays.toString(y));
        // }

        return map[n-1][m-1]%1000000007;
    }

    public static void main(String[] args) {
        int a = new Solution_bfs().solution(4, 3, new int[][]{{2, 2}});

        System.out.println(a);
    }
}
