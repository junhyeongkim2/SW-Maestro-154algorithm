import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String[] arr = Arrays.stream(numbers)
                .mapToObj(String::valueOf).toArray(String[]::new);

        Arrays.sort(arr, (o1,o2) -> (o2+o1).compareTo(o1+o2));

        if(arr[0].equals("0")) return "0";

        answer = Arrays.toString(arr).replaceAll("[^0-9]","");

        return answer;
    }

}