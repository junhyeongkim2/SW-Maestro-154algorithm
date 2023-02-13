import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        Arrays.sort(A);
        PriorityQueue<Integer> pq = Arrays.stream(B)
                .boxed()
                .sorted()
                .collect(Collectors.toCollection(PriorityQueue::new));

        for(int k : A){
            int n = -1;
            while(k >= n && !pq.isEmpty()){
                n = pq.poll();
            }
            if(n > k) answer++;
        }

        return answer;
    }
}