package 프로그래머스_고득점_kit.DFS_BFS.네트워크;

import java.util.*;

public class Solution {
    boolean[] visited;
    int answer = 0;

    public void bfs(int nn, int n, int[][] computers){
        Queue<Integer> q = new LinkedList<>();

        q.add(nn);

        while(!q.isEmpty()){
            int node = q.poll();
            for(int j = 0; j<computers[node].length; j++){
                if(computers[node][j]==1&&!visited[j]){
                    visited[j]=true;
                    q.add(j);
                }

            }

        }

    }


    public int solution(int n, int[][] computers) {

        visited = new boolean[n];

        for(int i = 0; i<n; i++){
            if(!visited[i]){
                answer++;
                bfs(i,n,computers);
            }
        }


        return answer;
    }
}
