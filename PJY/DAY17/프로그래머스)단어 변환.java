import java.util.*;

class Solution {
    int answer = 50;
    boolean[] arrived;

    public int solution(String begin, String target, String[] words) {
        List<String> list = Arrays.asList(words);
        if (!list.contains(target)) return 0;

        arrived = new boolean[words.length];
        searchWord(begin, target, words, 0);
        return answer;
    }

    public void searchWord(String begin, String target, String[] words, int n) {
        if (begin.equals(target)) answer = Math.min(n, answer);

        for (int i = 0; i < words.length; i++) {
            String now = words[i];
            if (!arrived[i] && validateWord(begin, now)) {
                arrived[i] = true;
                searchWord(now, target, words, n + 1);
                arrived[i] = false;
            }
        }
    }

    public boolean validateWord(String now, String begin) {
        int n = 0;

        for (int i = 0; i < now.length(); i++) {
            if (now.charAt(i) != begin.charAt(i)) n++;
        }

        if (n == 1) return true;
        return false;
    }
}