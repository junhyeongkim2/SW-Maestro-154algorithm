import java.util.*;

class Solution {
    int[] dx = {0,0,1,-1};
    int[] dy = {1,-1,0,0};

    public int solution(int[][] maps) {
        int answer = -1;
        int[][] arrived = new int[maps.length][maps[0].length];
        PriorityQueue<Vertex> pq = new PriorityQueue<>();

        pq.add(new Vertex(0,0,1));
        arrived[0][0] = 1;

        while(!pq.isEmpty()){
            Vertex now = pq.poll();
            if(now.x == maps.length-1 && now.y == maps[0].length-1){
                answer = now.value;
                break;
            }

            for(int i = 0; i<4; i++){
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                if(nx>=0 && ny>=0 && nx< maps.length && ny<maps[0].length){
                    if(arrived[nx][ny] == 0 && maps[nx][ny] == 1){
                        pq.add(new Vertex(nx, ny, now.value+1));
                        arrived[nx][ny] = 1;
                    }
                }
            }
        }

        return answer;
    }
    class Vertex implements Comparable<Vertex>{
        int x;
        int y;
        int value;

        public Vertex(int x, int y, int value) {
            this.x = x;
            this.y = y;
            this.value = value;
        }

        @Override
        public int compareTo(Vertex o) {
            return this.value - o.value;
        }
    }
}