import java.util.*;

class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int now = 0;
        int num = w*2 + 1;

        for(int station : stations){
            float k = station - w - now - 1;
            answer+= Math.ceil(k/num);
            now = station + w;
        }

        if(now > n) return answer;

        float k = n - now;
        answer+= Math.ceil(k/num);

        return answer;
    }
}