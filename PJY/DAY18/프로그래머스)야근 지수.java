import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;

        PriorityQueue pq = new PriorityQueue(Collections.reverseOrder());

        for(Integer i : works){
            pq.add(i);
        }

        for(int i = 0; i < n; i++){
            int k = (int) pq.poll() - 1;
            pq.add(k);
        }

        while(!pq.isEmpty()){
            int k = (int) pq.poll();
            if(k > 0) answer += Math.pow(k, 2);
        }

        return answer;
    }
}