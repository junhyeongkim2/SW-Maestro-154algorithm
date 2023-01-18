class Solution {
    public String solution(int n) {
        int[] arr = {4,1,2};
        String answer = "";

        StringBuilder sb = new StringBuilder();

        while(n > 0){
            sb.append(arr[n%3]);

            n = (n-1)/3;
        }

        answer = sb.reverse().toString();

        return answer;
    }
}