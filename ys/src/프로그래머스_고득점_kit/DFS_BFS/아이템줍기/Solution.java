package 프로그래머스_고득점_kit.DFS_BFS.아이템줍기;

import java.util.LinkedList;
import java.util.Queue;

public class Solution {

    /*
    1. 전체 도형의 바깥 부분 그리고
    2. 동서남북으로 최단 거리 -> bfs, queue 이용
    */
    int minX = 100, minY = 100, maxX = 0, maxY = 0;
    int[][] map;
    boolean[][] visited;
    int answer = 0;

    public void outline(int[][] rectangle){

        for(int i = 0; i<rectangle.length; i++){
            minX = Math.min(minX,rectangle[i][0]);
            minY = Math.min(minY,rectangle[i][1]);
            maxX = Math.max(maxX,rectangle[i][2]);
            maxY = Math.max(maxY,rectangle[i][3]);
        }

        map = new int[maxY*2+2][maxX*2+2];
        visited = new boolean[maxY*2+2][maxX*2+2];

        for(int r = 0 ; r<rectangle.length; r++){
            for(int i = rectangle[r][1]*2; i<=rectangle[r][3]*2; i++){
                for(int j = rectangle[r][0]*2; j<=rectangle[r][2]*2;j++){
                    map[i][j]++;
                }
            }
        }

        for(int i = 0; i<map.length; i++){
            for(int j = 0; j<map[i].length;j++){
                try{
                    if((map[i-1][j]==0||map[i+1][j]==0||map[i][j-1]==0||map[i][j+1]==0)&&map[i][j]==1){
                        map[i][j]=-1;
                    }
                } catch(Exception e) {continue;}
            }
        }

        for(int i = 0; i<map.length;i++){
            for(int j = 0;j<map[i].length; j++){
                System.out.printf("%3d",map[i][j]);
            }
            System.out.println();
        }

    }

    public void bfs(int cax, int cay, int ix, int iy) {
        Queue<int[]> q = new LinkedList<>();

        int[] dy = {0,1,0,-1};
        int[] dx = {1,0,-1,0};

        q.add(new int[]{cay*2,cax*2,1});
        visited[cay*2][cax*2] = true;

        while(!q.isEmpty()){
            int[] p = q.poll();

            int cy = p[0];
            int cx = p[1];
            int depth = p[2];

            if(cy==iy*2&&cx==ix*2){
                answer = depth/2;
                return;
            }

            for(int i = 0; i<4; i++){
                int ny = cy + dy[i];
                int nx = cx + dx[i];

                if(ny<0||nx<0||ny>maxY*2||nx>maxX*2) continue;

                if(map[cy][cx]==-1&&map[ny][nx]==-1&&!visited[ny][nx]){
                    visited[ny][nx] = true;
                    q.add(new int[]{ny,nx, depth+1});
                }

                if(map[cy][cx]==-1&&map[ny][nx]==2&&!visited[ny][nx]){
                    visited[ny][nx] = true;
                    q.add(new int[]{ny,nx, depth+1});
                }

                if(map[cy][cx]==2&&map[ny][nx]==-1&&!visited[ny][nx]){
                    visited[ny][nx] = true;
                    q.add(new int[]{ny,nx, depth+1});
                }

            }

        }
    }


    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {

        //바깥 부분 그리고
        outline(rectangle);


        //bfs 최단거리
        bfs(characterX, characterY, itemX, itemY);

        //확인
        System.out.println("========================================");
        for(int i = 0; i<map.length;i++){
            for(int j = 0;j<map[i].length; j++){
                if(visited[i][j]) System.out.printf("%3d",1);
                else System.out.printf("%3d",0);
            }
            System.out.println();
        }

        return answer;
    }

    public static void main(String[] args) {
        int a = new Solution().solution(new int[][]{{1, 1, 5, 7}}, 1,1,4,7);

        System.out.println(a);
    }
}

/**
 * 두배로 키웠을 때 범위 지정하는 부분에서 주위
 *  -> 모든 점을 포함해서 두배로 키워야함.
 *
 */