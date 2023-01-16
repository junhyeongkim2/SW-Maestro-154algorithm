import java.util.*;

class Solution {
    public String solution(String number, int k) {
        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < number.length(); i++){
            char c = number.charAt(i);

            while(!stack.isEmpty() && stack.peek() < c && k-- > 0){
                stack.pop();
            }

            stack.add(c);
        }

        if(stack.size() > number.length() - k) stack.pop();

        return stack.toString().replaceAll("[^0-9]","");
    }
}