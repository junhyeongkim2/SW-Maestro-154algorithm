package 프로그래머스_고득점_kit.완전탐색.모음사전;

import java.util.*;

public class Solution {
    /*
    맵 이용해서...
    a   e   i   o   u
    a   e   i   o   u
    a   e   i   o   u
    a   e   i   o   u
    a   e   i   o   u

    n자리 단어일 때,
    첫째 자리까지 수 : (5^4)+(5^3)+(5^2)+(5^1)+(5^0) * 알파벳 모음 번호 (a:0, e:1, i:2, o:3, u:4)
    둘째 자리까지 수 : (5^3)+(5^2)+(5^1)+(5^0) * 알파벳 모음 번호
    .
    .
    n번째 자리까지 수 : (5^(n-1))+...+(5^0) * 알파벳 모음 번호


    (첫째 자리까지 수 + ... + n번째 자리까지 수) + 총 자릿 수 = 단어 번호

    */

    String[] alp = new String[]{"A","E","I","O","U"};
    int[] score = new int[]{1,6,31,156,781};

    public int solution(String word) {
        int answer = 0;

        //단어 표
        String[][] wordMap = new String[5][5];
        for(int i = 0 ; i<5; i++){
            for(int j = 0; j<5; j++){
                wordMap[i][j] = alp[j];
            }
        }


        //각 자리수까지 계산, 마지막 알파벳에서 총 자릿수 더하기
        for(int d = 0 ; d<word.length();d++){

            String s = String.valueOf(word.charAt(d));
            int alp_index = 0;

            for(int i = 0; i<alp.length;i++){
                if(alp[i].equals(s)){
                    alp_index = i;
                }
            }

            if(d==word.length()-1){
                answer += score[5-d-1]*alp_index + d+1;
            } else {
                answer += score[5-d-1]*alp_index;
            }
        }


        return answer;
    }
}
