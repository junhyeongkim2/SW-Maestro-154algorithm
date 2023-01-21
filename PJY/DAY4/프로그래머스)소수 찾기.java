import java.util.*;

class Solution {
    Set<Integer> set = new HashSet<>();
    boolean[] visited;
    public int solution(String numbers) {
        int answer = 0;
        visited = new boolean[numbers.length()];

        addList(numbers, "");

        set.remove(0);
        set.remove(1);

        if(set.size() == 0) return answer;

        for(Integer i : set){
            for(int j = 2; j <= i; j++){
                if(i == j) answer++;
                if(i%j == 0) break;
            }
        }

        return answer;
    }

    public void addList(String numbers, String str){

        if(str.length() > numbers.length()) return;

        if(!str.equals("")) set.add(Integer.parseInt(str));

        for(int i = 0; i < numbers.length(); i++){
            if(visited[i]) continue;
            visited[i] = true;
            addList(numbers, str+numbers.charAt(i));
            visited[i] = false;
        }
    }
}