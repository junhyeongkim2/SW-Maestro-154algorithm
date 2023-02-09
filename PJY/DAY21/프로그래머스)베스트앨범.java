import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> map = new HashMap<>();
        Map<String, Integer> countMap = new HashMap<>();
        List<Integer> list = new ArrayList<>();
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < genres.length; i++) {
            map.put(genres[i], map.getOrDefault(genres[i], 0) + plays[i]);
            countMap.put(str, countMap.getOrDefault(str, 0) + 1);
            list.add(i);
        }

        list.sort((o1, o2) -> {
            if (map.get(genres[o2]) == map.get(genres[o1])) {
                if (plays[o2] == plays[o1]) return o1 - o2;
                return plays[o2] - plays[o1];
            }
            return map.get(genres[o2]) - map.get(genres[o1]);
        });

        for (int i = 0; i < genres.length; i++) {
            String str = genres[list.get(i)];
            countMap.put(str, countMap.getOrDefault(str, 0) + 1);
            if (countMap.get(str) < 3) result.add(list.get(i));
        }

        return result.stream().mapToInt(i -> i).toArray();
    }
}