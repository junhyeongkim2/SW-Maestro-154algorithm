class Solution {
    public int[] solution(int n, int s) {
        int[] answer = new int[n];

        for(int i = 0; i < answer.length; i++){
            answer[i] = s/n;
        }

        int k = s % n;

        for(int i = 0; i < k; i++){
            answer[answer.length - 1 - i]++;
        }

        if(s < n) return new int[]{-1};

        return answer;
    }
}