package 프로그래머스_고득점_kit.DFS_BFS.게임맵최단거리;

import java.util.LinkedList;
import java.util.Queue;

public class Solution {
//    public int solution(int[][] maps) {
//        int x = maps[0].length;
//        int y = maps.length;
//        int [][] visited = new int[y][x];
//
//
//        bfs(maps, visited);
//
//        int ans = visited[y - 1][x - 1];
//
//        if (ans == 0) {
//            ans = -1;
//        }
//
//        return ans;
//    }
//
//    public void bfs(int[][] map, int[][] visited) {
//
//        int[] dx = {1, 0, -1, 0};
//        int[] dy = {0, 1, 0, -1};
//
//        int x = 0;
//        int y = 0;
//        visited[x][y] = 1;
//        Queue<int[]> queue = new LinkedList<>();
//        queue.add(new int[]{y, x});
//
//        while (!queue.isEmpty()) {
//            int[] current = queue.poll();
//            int cX = current[1];
//            int cY = current[0];
//
//            for (int i = 0; i < 4; i++) {
//                int nx = cX + dx[i];
//                int ny = cY + dy[i];
//
//                if (nx < 0 || nx > map[0].length - 1 || ny < 0 || ny > map.length - 1) {
//                    continue;
//                }
//
//                if (map[ny][nx] == 1 && visited[ny][nx] == 0) {
//                    visited[ny][nx] = visited[cY][cX] + 1;
//                    queue.offer(new int[]{ny, nx});
//                }
//
//            }
//        }
//    }

    int answer = 0;
    int[] dx = new int[]{1,0,-1,0};
    int[] dy = new int[]{0,-1,0,1};
    boolean[][] visit;

    public void bfs(int depth, int[][] maps){

        Queue<int[]> q = new LinkedList<>();

        q.add(new int[]{0,0,0});

        while(!q.isEmpty()){

            int[] p = q.poll();

            for(int i = 0; i<4; i++){
                int py = p[0]+dy[i];
                int px = p[1]+dx[i];
                int d = p[2];

                if(p[0]==maps.length&&p[1]==maps[0].length&&visit[p[0]][p[1]]){
                    answer = d;
                    return;
                }

                if(py<0||px<0||py>=maps.length||px>=maps[0].length) continue;


                if(maps[py][px]==1&&!visit[py][px]){
                    visit[py][px]=true;
                    q.add(new int[]{py,px,d+1});
                }

            }

        }

        answer = -1;

    }


    public int solution(int[][] maps) {

        visit = new boolean[maps.length][maps[0].length];
        visit[0][0] = true;
        bfs(0,maps);


        return answer;
    }

    public static void main(String[] args) {
        int a = new Solution().solution(new int[][]{{1, 0, 1, 1, 1},{1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,1},{0,0,0,0,1}});

        System.out.println(a);
    }

}

