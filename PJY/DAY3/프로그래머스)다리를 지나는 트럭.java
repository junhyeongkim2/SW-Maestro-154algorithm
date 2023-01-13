import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        List<Integer> list = Arrays.stream(truck_weights)
                .boxed().collect(Collectors.toList());

        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < bridge_length; i++) {
            q.add(0);
        }

        int answer = 0;

        while (!list.isEmpty() || !q.isEmpty()) {
            weight += q.poll();
            answer++;

            if (list.isEmpty()) continue;

            int n = 0;

            if (list.get(0) <= weight) {
                weight -= list.get(0);
                n = list.remove(0);
            }

            q.add(n);
        }

        return answer;
    }
}