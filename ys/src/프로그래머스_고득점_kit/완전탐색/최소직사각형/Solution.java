package 프로그래머스_고득점_kit.완전탐색.최소직사각형;

public class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;

        int max_w = Math.max(sizes[0][0],sizes[0][1]);
        int max_h = Math.min(sizes[0][0],sizes[0][1]);

        for(int i =0; i<sizes.length;i++){
            int max = Math.max(sizes[i][0],sizes[i][1]);
            int min = Math.min(sizes[i][0],sizes[i][1]);

            sizes[i][0] = max;
            sizes[i][1] = min;
        }

        for(int i = 0; i<sizes.length;i++){
            System.out.printf("%d %d, ",sizes[i][0],sizes[i][1]);
            if(max_w<sizes[i][0]) max_w=sizes[i][0];
            if(max_h<sizes[i][1]) max_h=sizes[i][1];
        }

        System.out.printf("\n %d %d",max_w,max_h);
        return max_w*max_h;
    }
}