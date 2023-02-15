package 프로그래머스_고득점_kit.완전탐색.피로도;

import java.util.*;

/*
* 1. 최댓값을 구해야하므로 dfs로
* 2. 방문 arr 만들고
* 3. depth로 비교
* */

public class Solution {
    int ans = 0;
    boolean[] visit;

    public void dfs(int depth, int hp, int[][]dungeons){
        for (int i = 0; i < dungeons.length; i++) {
            if(!visit[i]&&dungeons[i][0]<=hp){
                visit[i]=true;
                dfs(depth+1,hp-dungeons[i][1],dungeons);
                visit[i]=false;
            }
        }

        ans = Math.max(ans,depth);
    }

    public int solution(int k, int[][] dungeons) {

        visit = new boolean[dungeons.length];
        dfs(0,k,dungeons);

        return ans;
    }



    public static void main(String[] args) {
        int a = new Solution().solution(80, new int[][]{{80, 20}, {50, 40}, {30, 10}});
        System.out.println(a);
    }
}