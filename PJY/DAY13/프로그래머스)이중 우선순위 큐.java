import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        PriorityQueue<Integer> minQ = new PriorityQueue<>();
        PriorityQueue<Integer> maxQ = new PriorityQueue<>((o1,o2) -> o2 - o1);

        for(String operation : operations){
            boolean tf = minQ.isEmpty() || maxQ.isEmpty();

            if(!tf && operation.equals("D -1")) {
                int min = minQ.poll();
                maxQ.remove(min);
            } else if(!tf && operation.equals("D 1")){
                int max = maxQ.poll();
                minQ.remove(max);
            } else if(operation.contains("I")){
                int n = Integer.parseInt(operation.replaceAll("[^0-9-]",""));
                maxQ.add(n);
                minQ.add(n);
            }

        }

        if(!maxQ.isEmpty()) answer[0] = maxQ.peek();
        if(!minQ.isEmpty()) answer[1] = minQ.peek();

        return answer;
    }
}