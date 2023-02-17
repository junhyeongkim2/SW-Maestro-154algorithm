package 프로그래머스_고득점_kit.완전탐색.전력망을_둘로_나누기;
import java.util.*;

public class Solution {static int[][] arr;
    public int solution(int n, int[][] wires) {
        int answer = n;
        arr= new int[n+1][n+1];

        //1. 인접행렬에 input
        for(int i=0; i<wires.length; i++){
            arr[wires[i][0]][wires[i][1]]=1;
            arr[wires[i][1]][wires[i][0]]=1;
        }

        //2. 선을 하나씩 끊어보며 순회
        int a, b;
        for(int i=0; i<wires.length; i++){
            a= wires[i][0];
            b= wires[i][1];

            //선을 하나 끊고
            arr[a][b]=0;
            arr[b][a]=0;

            //bfs
            answer= Math.min(answer, bfs(n, a));

            //선 다시 복구
            arr[a][b]=1;
            arr[b][a]=1;
        }

        return answer;
    }

    public int bfs(int n, int start){
        int[] visit= new int[n+1];
        int cnt=1;

        Queue<Integer> queue= new LinkedList<>();
        queue.offer(start);

        while(!queue.isEmpty()){
            int point= queue.poll();
            visit[point]= 1;

            for(int i=1; i<=n; i++){ //point와 연결된 애들 중에 방문한적 없는 노드 전부 큐에 넣기
                if(visit[i]==1) continue;
                if(arr[point][i]==1) {
                    queue.offer(i);
                    cnt++;
                }
            }
        }
        return (int)Math.abs(n-2*cnt); //cnt-(n-cnt);
    }//bfs

    public static void main(String[] args) {
        int a = new Solution().solution(9,new int[][]{{1,3},{2,3},{3,4},{4,5},{4,6},{4,7},{7,8},{7,9}});
        //[[1,2],[1,3],[1,4],[4,5],[5,6],[6,7],[6,8]]
        int b = new Solution().solution(8,new int[][]{{1,2},{1,3},{1,4},{4,5},{5,6},{6,7},{6,8}});
        //n =6, wires = [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]], answer = 2
        int c = new Solution().solution(6,new int[][]{{1,4},{6,3},{2,5},{5,1},{5,3}});
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
}
