import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        Map<String, Integer> map = new HashMap<>();

        for(int i = 0; i < want.length; i++){
            map.put(want[i], number[i]);
        }

        for(int i = 0; i < discount.length - 9; i++){
            Map<String, Integer> copy = new HashMap<>(map);

            boolean tf = true;

            for(int j = i; j < i+10; j++){
                String item = discount[j];
                int count = copy.getOrDefault(item, 0);

                if(count == 0) {
                    tf = false;
                    break;
                }
                copy.put(item, count-1);
            }

            if(tf) answer++;
        }

        return answer;
    }
}
