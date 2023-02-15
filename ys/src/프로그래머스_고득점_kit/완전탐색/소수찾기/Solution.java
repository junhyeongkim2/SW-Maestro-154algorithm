package 프로그래머스_고득점_kit.완전탐색.소수찾기;

import java.util.*;

public class Solution {
    HashSet<Integer> set = new HashSet<>();

    public void recursive(String comb, String others){
        if(comb!=""){
            set.add(Integer.valueOf(comb));
        }

        for(int i = 0; i<others.length();i++){
            recursive(comb+others.charAt(i),others.substring(0,i)+others.substring(i+1));
        }
    }

    public boolean isPrime(int num){

        if(num==0||num==1){
            return false;
        }

        int lim = (int)Math.sqrt(num);

        for(int i = 2;i<=lim;i++){
            if(num%i==0){
                return false;
            }
        }

        return true;
    }

    public int solution(String numbers) {
        int answer = 0;

        recursive("",numbers);
        // System.out.print(set);

        Iterator<Integer> it = set.iterator();

        while(it.hasNext()){

            int temp = it.next();

            if(isPrime(temp)){
                answer++;
            }
        }


        return answer;
    }

    public static void main(String[] args) {
        int a = new Solution().solution("17");
        int b = new Solution().solution("011");
        System.out.println(a);
        System.out.println(b);
    }
}
