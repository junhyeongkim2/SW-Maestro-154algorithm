package 프로그래머스_고득점_kit.DP.정수삼각형;

import java.util.Arrays;

public class Solution {

    public int solution(int[][] triangle) {

        for(int i = 1; i<triangle.length;i++){

            if(i==1){
                triangle[1][0] = triangle[0][0] + triangle[1][0];
                triangle[1][1] = triangle[0][0] + triangle[1][1];
            } else{
                for(int j = 0; j<triangle[i].length;j++){
                    if(j==0){
                        triangle[i][j] = triangle[i-1][j] + triangle[i][j];
                    } else if(j==triangle[i].length-1){
                        triangle[i][j] = triangle[i-1][j-1] + triangle[i][j];
                    } else{
                        triangle[i][j] = Math.max(triangle[i-1][j-1] + triangle[i][j],triangle[i-1][j] + triangle[i][j]);
                    }
                }
            }
        }

        return Arrays.stream(triangle[triangle.length-1]).max().getAsInt();
    }
}

/* dfs, but 시간 초과....
import java.util.*;

class Solution {
    boolean[][] visited;
    int answer = 0;

    public void dfs(int[][] triangle, int depth, int total, int idx){
        if(depth==triangle.length){
            answer = Math.max(answer,total);
            return;
        }

        for(int j = 0 ; j<triangle[depth].length;j++){
            if(j==idx || j==idx+1){
                if(!visited[depth][j]){
                    visited[depth][j] = true;
                    dfs(triangle, depth+1, total+triangle[depth][j],j);
                    visited[depth][j] = false;
                    }
            }
        }



    }

    public int solution(int[][] triangle) {

        visited = new boolean[triangle.length][0];

        for(int i = 0; i<triangle.length; i++){

            int cnt = 0;
            for(int j = 0; j<triangle[i].length; j++){
                cnt++;
            }

            visited[i] = new boolean[cnt];
        }

        dfs(triangle,0,0,0);

        return answer;
    }
}
*/


/* 기존 풀이:python
import copy


def solution(triangle):
    answertemp = [[]*500 for _ in range(500)]
    temptriangle = copy.deepcopy(triangle)

    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            nextJ1 = j
            nextJ2 = j+1

            temp1 = temptriangle[i][j] + triangle[i+1][nextJ1]
            temp2 = temptriangle[i][j] + triangle[i+1][nextJ2]

            if(temptriangle[i + 1][nextJ1] < temp1):
                temptriangle[i + 1][nextJ1] = temp1

            if (temptriangle[i + 1][nextJ2] < temp2):
                temptriangle[i + 1][nextJ2] = temp2

            # print("triangle[i][j], triangle[i+1][nextJ1], triangle[i+1][nextJ2] :", triangle[i][j], triangle[i+1][nextJ1], triangle[i+1][nextJ2])
            # print("temp1, temp2", temp1, temp2)
            answertemp[i].append(temp1)
            answertemp[i].append(temp2)


    return max(answertemp[len(triangle)-2])


*/
