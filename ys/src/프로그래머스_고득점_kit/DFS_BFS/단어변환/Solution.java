package 프로그래머스_고득점_kit.DFS_BFS.단어변환;
import java.util.*;

public class Solution {
    int answer = 0;
    boolean[] visited;

    public void bfs(String begin, String target, String[] words){

        Queue<String[]> q = new LinkedList<>();

        q.add(new String[]{begin,String.valueOf(answer)});

        while(!q.isEmpty()){
            String[] toCheck = q.poll();
            String check = toCheck[0];
            int depth = Integer.valueOf(toCheck[1]);

            if(check.equals(target)){
                answer = depth;
                return;
            }

            for(int i = 0; i<words.length;i++){
                if(!visited[i]){

                    int cnt = 0;
                    for(int j = 0; j<words[i].length();j++){
                        if(words[i].charAt(j) != check.charAt(j)){
                            cnt++;
                        }
                    }

                    if(cnt<2){
                        visited[i] = true;
                        q.add(new String[] {words[i], String.valueOf(depth+1)});
                    }


                }
            }

        }


    }

    public int solution(String begin, String target, String[] words) {

        // >> 가능 여부 확인
        boolean flag = false;

        for(String s : words){
            if(s.equals(target)){
                flag = true;
            }
        }

        if(!flag){
            return 0;
        }
        // 가능 여부 확인 <<

        visited = new boolean[words.length];
        bfs(begin,target,words);

        return answer;
    }
}
