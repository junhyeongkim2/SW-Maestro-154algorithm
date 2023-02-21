package 프로그래머스_고득점_kit.DFS_BFS.여행경로;
import java.util.*;

public class Solution {
    String[] answer;
    boolean[] used;

    public class Ticket implements Comparable<Ticket>{
        String from;
        String to;
        int idx;

        public Ticket(String from, String to, int idx){
            this.from = from;
            this.to = to;
            this.idx = idx;
        }

        public String getFrom(){
            return from;
        }

        public String getTo(){
            return to;
        }

        public int getIdx(){
            return idx;
        }


        @Override
        public int compareTo(Ticket t){
            if(this.to.compareTo(t.to)>0){
                return 1;
            } else if(this.to.compareTo(t.to)<0){
                return -1;
            } else return 0;
        }

    }

    public void dfs(String start, String[][] tickets, int depth){
        if(depth==tickets.length){
            return;
        }

        List<Ticket> canGo = new ArrayList<>();

        for(int i = 0; i<tickets.length; i++){
            if(tickets[i][0].equals(start)&&!used[i]){
                canGo.add(new Ticket(tickets[i][0], tickets[i][1], i));
            }
        }

        Collections.sort(canGo);

        for(int i = 0; i<canGo.size();i++){
            Ticket temp = canGo.get(i);

            used[temp.getIdx()] = true;
            answer[depth] = temp.getFrom();

            if(depth==tickets.length-1){
                answer[depth+1] = temp.getTo();
                return;
            }

            dfs(temp.getTo(), tickets, depth+1);

            if(answer[answer.length-1]==null){
                used[temp.getIdx()] = false;
            } else return;
        }


    }

    public String[] solution(String[][] tickets) {
        answer = new String[tickets.length+1];
        used = new boolean[tickets.length];

        dfs("ICN", tickets, 0);


        return answer;
    }

    public static void main(String[] args) {
        String[] a = new Solution().solution(new String[][]{{"ICN", "SFO"}, {"ICN", "ATL"},{"SFO", "ATL"},{"ATL", "ICN"},{"ATL", "SFO"}});

        for(String s : a){
            System.out.print(s+", ");
        }

    }
}

/**
 * 1.
 *  무조건 알파벳 순으로 추가하면 안됨.
 *  a,b / b,a / b,c / a,c
 *  모든 티켓 사용 불가.
 *
 *  모든 티켓을 사용하는 조건이 우선,
 *  이후 알파벳 순으로 정렬해야함.
 *
 *  2.
 *  comparTo Override 활용하는 방법 다시 확인.
 *  (참조)
 *  https://wjheo.tistory.com/entry/Java-%EC%A0%95%EB%A0%AC%EB%B0%A9%EB%B2%95-Collectionssort
 *
 *
 *  3. List 안에 객체 사용하는게 더 편리한듯
 *      - 이전에는 String[], int[] 등을 이용했음
 *      - 객체 사용하면 String, int를 조합해서 사용 가능.
 *      - 단, 객체 사용시, getter setter constructor 추가할 것(살짝 귀찮..)
 */

/*
* 깔끔한 풀이 1
import java.util.ArrayList;
import java.util.Collections;
class Solution {
    static boolean[] visit;
    static ArrayList<String> list=new ArrayList<>();
    public String[] solution(String[][] tickets) {
        visit = new boolean[tickets.length];
        DFS(0, "ICN", "ICN", tickets);
        Collections.sort(list);
        String[] temp = list.get(0).split(" ");
        return temp;
    }

    private static void DFS(int cnt, String from, String word, String[][] tickets) {
        if (cnt == tickets.length) {

            list.add(word);

        }else{
            for (int i = 0; i < tickets.length; i++) {
                if (!visit[i] && tickets[i][0].equals(from)) {
                    visit[i]=true;
                    DFS(cnt+1,tickets[i][1],word+" "+tickets[i][1],tickets);
                    visit[i]=false;
                }
            }
        }
    }
}
* */

