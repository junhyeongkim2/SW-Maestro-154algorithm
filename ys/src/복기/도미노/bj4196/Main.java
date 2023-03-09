package 복기.도미노.bj4196;

import java.util.*;

public class Main {

    public static class status{
        int childCnt;
        List<Integer> idxs;

        public status(int childCnt, List<Integer> idxs){
            this.childCnt = childCnt;
            this.idxs = idxs;
        }
    }

    public static class branch3Idx{
        int[] relation;
        int idx;
        int cnt;

        public branch3Idx(int[] relation, int idx, int cnt){
            this.relation = relation;
            this.idx = idx;
            this.cnt = cnt;
        }
    }

    public boolean isFinished(boolean[] bfsVisited){

        for(boolean x : bfsVisited){
            if(!x){
                return false;
            }
        }

        return true;
    }

    public status bfs(int[][]branch, int start, int total, boolean[] bfsVisited) {
        Queue<branch3Idx> q = new LinkedList<>();
        int childCnt = 0;
        List<Integer> idxs = new ArrayList<>();
        boolean[] visitedTemp = bfsVisited.clone();

        q.add(new branch3Idx(branch[start],start,1));
        visitedTemp[start] = true;
        int cnt = 1;

        while(!q.isEmpty()){
            branch3Idx bi = q.poll();
            int[] r = bi.relation;
//            int cnt = bi.cnt;

            idxs.add(bi.idx);
//            childCnt = cnt;

            int head = r[0];
            int tail = r[1];

            for(int i = 0; i<branch.length; i++){
                if(!visitedTemp[i]&&branch[i][0]==tail){
//                    q.add(new branch3Idx(branch[i], i, cnt+1));
                    q.add(new branch3Idx(branch[i], i, cnt++));
                    visitedTemp[i] = true;
                }
                if(!visitedTemp[i]&&branch[i][1]==head){
//                    q.add(new branch3Idx(branch[i], i, cnt+1));
                    q.add(new branch3Idx(branch[i], i, cnt++));
                    visitedTemp[i] = true;
                }
            }

        }
        childCnt = cnt;

        return new status(childCnt,idxs);
    }

    public int solution(int n, int m, int[][] branch) {
        int answer = 0;
        boolean[] bfsVisitedMain = new boolean[branch.length];


        while (!isFinished(bfsVisitedMain)){
            status best = new status(0,new ArrayList<>());

            for (int i = 0; i < m; i++) {
                if(!bfsVisitedMain[i]){
                    status temp = bfs(branch,i,n, bfsVisitedMain);

                    if(best.childCnt<temp.childCnt){
                        best = temp;
                    }
                }
            }

            for(Integer j : best.idxs){
                bfsVisitedMain[j] = true;
            }

            answer++;

        }

        return answer;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int caseNum = sc.nextInt();


        for (int i = 0; i < caseNum; i++) {
            int n = sc.nextInt();
            int m = sc.nextInt();

            int[][] branch = new int[m][2];
            for (int j = 0; j < m; j++) {
                branch[j][0] = sc.nextInt();
                branch[j][1] = sc.nextInt();
            }

            System.out.println(new Main().solution(n, m, branch));
        }

    }
}
