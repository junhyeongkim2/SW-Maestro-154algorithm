package 프로그래머스_고득점_kit.정렬.H인덱스;

import java.util.*;

public class Solution {
    public int solution(int[] citations) {
        int answer = 0;


        Arrays.sort(citations);


        for(int i = 0 ; i<citations.length; i++){
            int h = citations.length - i;
            boolean flag = true;


            for(int j = i; j<citations.length; j++){
                if(citations[j]<h){
                    flag = false;
                    break;
                }
            }

            if(flag) {
                return h;
            }
        }


        return answer;
    }
}
