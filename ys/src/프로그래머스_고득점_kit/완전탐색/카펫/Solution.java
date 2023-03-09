package 프로그래머스_고득점_kit.완전탐색.카펫;

import java.util.*;

public class Solution {

    /*
    x*y라고 할때,
    (x-2)*(y-2)=노랑색 갯수
    x*y-(x-2)*(y-2)=갈색 갯수

    노랑색 + 갈색 = (x-2)*(y-2)+x*y-(x-2)*(y-2) = xy

    browm = x+x+(2*yellow_y)
    yellow = (x-2)*yellow_y

    xy = 2*x+2yy+x*yy-2yy = x*(2+yy)
    */

    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        List<Integer> l = new ArrayList<>();

        int total = brown+yellow;

        for(int i =1; i<=yellow;i++){
            if(yellow%i==0){

                if(total%(i+2)==0){

                    int x = total/(i+2);

                    if(x+x+2*i==brown){
                        l.add(x);
                        l.add(i+2);
                        break;
                    }
                }
            }
        }



        return l.stream().mapToInt(Integer::intValue).toArray();
    }
}