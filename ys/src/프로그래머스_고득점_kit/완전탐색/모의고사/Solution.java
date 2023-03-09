package 프로그래머스_고득점_kit.완전탐색.모의고사;

import java.util.*;

public class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        List<Integer> l = new ArrayList<>();

        int[] sp1 = new int[]{1,2,3,4,5};
        int[] sp2 = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
        int[] sp3 = new int[]{3,3,1,1,2,2,4,4,5,5};

        int cnt1 = 0;
        int cnt2 = 0;
        int cnt3 = 0;

        for(int i = 0; i < answers.length; i++){
            if(answers[i]==sp1[i%5]){
                cnt1++;
            }
            if(answers[i]==sp2[i%8]){
                cnt2++;
            }
            if(answers[i]==sp3[i%10]){
                cnt3++;
            }
        }

        int max = Math.max(cnt1,Math.max(cnt2,cnt3));
        if(max==cnt1) l.add(1);
        if(max==cnt2) l.add(2);
        if(max==cnt3) l.add(3);



        return l.stream().mapToInt(Integer::intValue).toArray();
    }
}
