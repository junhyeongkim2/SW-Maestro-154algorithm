package 프로그래머스_고득점_kit.greedy.큰수만들기;

public class Solution {
    /*
    1. 1자리 수가 2번재 자리 수 보다 작을 경우 무조건 1째꺼 제거
    2. 0or감소 마지막 수 제거
    */

    /*
        StringBuffer
        - 멀티 쓰레드 환경에서 쓰레드 세이프를 지원한다.
        - 빠름
        StringBuilder
        - 멀티 쓰레드 환경에서 쓰레드 세이프를 지원하지 않는다.
        - 아주 빠름

        (참조)
        https://inpa.tistory.com/entry/JAVA-%E2%98%95-String-StringBuffer-StringBuilder-%EC%B0%A8%EC%9D%B4%EC%A0%90-%EC%84%B1%EB%8A%A5-%EB%B9%84%EA%B5%90
        */

    public String solution(String number, int k) {

        // StringBuffer answer = new StringBuffer(number);
        StringBuilder answer = new StringBuilder(number);

        while(k>0){
            boolean isMinus = false;
            boolean isSame = false;

            // 1. 1번째 자리 수가 2번재 자리 수 보다 작을 경우 무조건 1번째꺼 제거
            if(answer.charAt(0)<answer.charAt(1)){
                answer.deleteCharAt(0);

            } else{
                for(int i = 0; i<answer.length()-1;i++){
                    //마지막까지 제거된 수가 없는 경우,
                    // 마지막에서 2개의 수 비교 후 작은 수 제거
                    if(i==answer.length()-2){
                        if(answer.charAt(i)<answer.charAt(i+1)){
                            answer.deleteCharAt(i);
                        } else{
                            answer.deleteCharAt(i+1);
                        }
                        break;
                    } else if(i==0){
                        if(answer.charAt(0)<answer.charAt(1)){
                            answer.deleteCharAt(0);
                            break;
                        }
                    }

                    //2. 제거 :
                    //  - 같은 값 이후 증가시 증가 직전값
                    //  - 감소 이후 같은 값
                    //  - 감소의 마지막 값
                    // 이떼, 해당 지점을 세이브 하고 -> 세이브 포인트 부터 다시 제거 조건 검색.
                    // (앞쪽에서 지워지지 않은 조건을 다시 탐색할 필요가 없음.)
                    if(answer.charAt(i)>answer.charAt(i+1)){
                        isMinus = true;
                    }
                    else if(answer.charAt(i)==answer.charAt(i+1)){
                        isSame = true;
                    }

                    if((isMinus||isSame)&&answer.charAt(i)<answer.charAt(i+1)){
                        answer.deleteCharAt(i);
                        k--;
                        if(k>0){
                            i = i-2;
                        } else break;
                    }
                }
            }

            k--;
        }

        return answer.toString();
    }

    public static void main(String[] args) {
        String a = new Solution().solution("1924",2);

        System.out.println(a);
    }
}
