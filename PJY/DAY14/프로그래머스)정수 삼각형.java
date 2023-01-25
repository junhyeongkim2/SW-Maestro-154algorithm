import java.util.*;

class Solution {
    public int solution(int[][] triangle) {

        for(int i = 1; i < triangle.length; i++){
            for(int j = 0; j < triangle[i].length; j++)
                triangle[i][j] += findNumber(triangle,i, j);
        }

        return Arrays.stream(triangle[triangle.length-1]).max().getAsInt();
    }

    public int findNumber(int[][] triangle,int i, int j){
        if(j == 0) return triangle[i-1][j];
        if(j == triangle[i].length - 1) return triangle[i-1][j-1];

        return Math.max(triangle[i-1][j-1], triangle[i-1][j]);
    }
}