class Solution {
    boolean[] arrived;

    public int solution(int n, int[][] computers) {
        int answer = 0;
        arrived = new boolean[computers.length];
        for (int i = 0; i < computers.length; i++) {
            if (!arrived[i]) {
                network(i, computers);
                answer++;
            }
        }
        Arr
        return answer;
    }

    public void network(int n, int[][] computers) {
        for (int i = 0; i < computers[n].length; i++) {
            if (!arrived[i] && computers[n][i] == 1) {
                arrived[i] = true;
                network(i, computers);
            }
        }
    }
}
