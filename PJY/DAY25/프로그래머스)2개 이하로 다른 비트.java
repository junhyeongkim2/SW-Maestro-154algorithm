class Solution {
    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];

        for(int i = 0; i < numbers.length; i++){
            answer[i] = Long.MAX_VALUE;

            if(numbers[i]%2 == 0) {
                answer[i] = numbers[i]+1;
                continue;
            }

            String str = Long.toBinaryString(numbers[i]);

            int k = str.lastIndexOf("0");

            if(k == -1) str = "10"+str.substring(1);
            else str = str.substring(0,k)+"10"+str.substring(k+2);

            answer[i] = Long.parseLong(str,2);
        }

        return answer;
    }
}