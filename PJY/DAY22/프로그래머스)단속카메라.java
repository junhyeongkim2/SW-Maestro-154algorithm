import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        int num = -30001;
        Arrays.sort(routes, (o1,o2) -> {
            if(o1[1] == o2[1]) return o1[0] - o2[0];
            return o1[1] - o2[1];
        });

        for(int[] route : routes){
            if(num < route[0]){
                answer++;
                num = route[1];
            }
        }

        return answer;
    }
}