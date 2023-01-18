import java.util.*;

class Solution {
    int count = 0;
    int answer = 0;
    public int solution(String word) {
        char[] arr = { 'A', 'E', 'I', 'O', 'U'};

        addWord(arr, "", word);

        return answer;
    }

    public void addWord(char[] arr, String result, String word){
        if(answer != 0) return;
        if(result.length() > 5) return;

        if(result.equals(word)){
            answer = count;
            return;
        }

        count++;

        for(int i = 0; i < arr.length; i++){
            addWord(arr, result+arr[i], word);
        }
    }
}