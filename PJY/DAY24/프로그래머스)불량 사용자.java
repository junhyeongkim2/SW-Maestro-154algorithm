import java.util.*;

class Solution {
    List<List<String>> arr = new ArrayList<>();
    Set<Set<String>> result = new HashSet<>();

    public int solution(String[] user_id, String[] banned_id) {

        for (int k = 0; k < banned_id.length; k++) {
            String ban = banned_id[k];
            List<String> list = new ArrayList();

            for (int i = 0; i < user_id.length; i++) {
                boolean tf = true;
                String user = user_id[i];

                if (user.length() != ban.length()) continue;

                for (int j = 0; j < ban.length(); j++) {
                    char c = ban.charAt(j);
                    if (c != '*' && c != user.charAt(j)) {
                        tf = false;
                        break;
                    }
                }

                if (tf) list.add(user);
            }
            arr.add(list);
        }

        bfs(0, new HashSet<String>());

        return result.size();
    }

    public void bfs(int n, Set<String> set) {
        if (n == arr.size()) {
            result.add(new HashSet<>(set));
            return;
        }

        for (int j = 0; j < arr.get(n).size(); j++) {
            String str = arr.get(n).get(j);
            if (!set.contains(str)) {
                set.add(str);
                bfs(n + 1, set);
                set.remove(str);
            }
        }
    }
}