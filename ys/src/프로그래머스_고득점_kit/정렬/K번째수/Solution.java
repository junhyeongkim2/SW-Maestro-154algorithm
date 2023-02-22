package 프로그래머스_고득점_kit.정렬.K번째수;

import java.util.Arrays;

public class Solution {

    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];


        for(int i = 0; i<commands.length;i++){
            int[] temp = Arrays.copyOfRange(array,commands[i][0]-1,commands[i][1]);
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2]-1];
        }

        return answer;
    }

}

/**
 * 1.
 * Arrays.copyOfRange() -> 배열 깊은 복사, 부분 선택 가능
 */


/* 기존 답
import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for(int x = 0; x<commands.length;x++){
            int i = commands[x][0];
            int j = commands[x][1];
            int k = commands[x][2];

            List<Integer> temp = new ArrayList<>();

            for(int y=i; y<=j;y++){
                temp.add(array[y-1]);
            }

            temp.sort(Comparator.naturalOrder());

            answer[x] = temp.get(k-1);

        }

        return answer;
    }
}
*/