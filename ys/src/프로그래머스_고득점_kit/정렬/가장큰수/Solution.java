package 프로그래머스_고득점_kit.정렬.가장큰수;

import java.util.Arrays;
import java.util.Comparator;

public class Solution {
    public String solution(int[] numbers) {
        String answer = "";

        String[] str = new String[numbers.length];
        for(int i = 0 ; i<numbers.length; i++){
            str[i] = String.valueOf(numbers[i]);
        }

        Arrays.sort(str, new Comparator<String>(){
            @Override
            public int compare(String str1, String str2){
                return (str2+str1).compareTo(str1+str2);
            }
        });

        for(int i = 0 ; i<str.length; i++){
            answer += str[i];
        }

        // if(Integer.parseInt(answer)) return "0";
        // -> 정답이 너무 큰 경우 런타임에러 발생
        if(answer.charAt(0)=='0') return "0";

        return answer;
    }
}


/* 1트 : 시간/메모리 초과

//    1. dfs 이용해서 모든 수 배열에 저장
//    2. sort
//    3. 마지막 수 출력

String answer = "";
    boolean[] visited;
    public void dfs(int[] numbers, int depth, String result){
        if(depth==numbers.length){
            if(answer.equals("")){
                answer = "0";
            }
            answer = String.valueOf(Math.max(Integer.parseInt(answer),Integer.parseInt(result)));
        }

        for(int i = 0; i<numbers.length; i++){
            if(!visited[i]){
                visited[i] = true;
                dfs(numbers, depth+1, result+String.valueOf(numbers[i]));
                visited[i] = false;
            }


        }
    }

    public String solution(int[] numbers) {

        visited = new boolean[numbers.length];
        dfs(numbers, 0, "");

        return answer;
    }
*/



/* 기존 답
import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        //문자열 리턴을 해줄 스트링배열 생성
        String[] str = new String[numbers.length];

        //int배열 String배열로 변환
        for(int i = 0; i < numbers.length; i++){
            str[i] = String.valueOf(numbers[i]);
        }

        //내림차순 정렬
        Arrays.sort(str, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                return (b+a).compareTo(a+b);
                //오름차순 정렬 (o1+o2).compareTo(o1+o2);
            }
        });

        //0값이 중복일경우 ex){0,0,0}
        //답이 000이 나오면 안되므로 첫번째값이 0이면 0을 리턴
        if (str[0].equals("0")) return "0";

        //0이 아니면 문자열을 더해준다.
        for(String s: str) answer += s;

        return answer;
    }
}


*/