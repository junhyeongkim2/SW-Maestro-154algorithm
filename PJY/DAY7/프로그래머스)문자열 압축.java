import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = s.length();
        for(int i = 1; i <= s.length()/2; i++){
            String em = s.substring(0, i);
            StringBuilder sb = new StringBuilder();
            int count = 1;
            int x = 0;

            for(int j = i; j <= s.length()-i; j+=i){
                String e = s.substring(j,j+i);
                if(em.equals(e)){
                    count++;
                }else{
                    sb.append(em);
                    if(count != 1)sb.append(count);
                    count = 1;
                    em = e;
                }
                x = j+i;
            }
            sb.append(em);
            if(count != 1)sb.append(count);
            sb.append(s.substring(x));
            answer = Math.min(sb.length(),answer);
        }

        return answer;
    }
}