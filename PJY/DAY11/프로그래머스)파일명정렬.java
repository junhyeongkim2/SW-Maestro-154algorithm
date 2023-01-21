import java.util.*;

class Solution {
    public String[] solution(String[] files) {
        String[] answer = {};
        List<Vertex> list = new ArrayList<>();
        List<Character> cList = Arrays.asList('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');

        for (int i = 0; i < files.length; i++) {
            String file = files[i];
            boolean tf = false;
            StringBuilder head = new StringBuilder();
            StringBuilder number = new StringBuilder();
            StringBuilder tail = new StringBuilder();

            for (int j = 0; j < file.length(); j++) {
                char c = file.charAt(j);

                if (tf && !cList.contains(c)) {
                    tail.append(file.substring(j));
                    break;
                }

                if (cList.contains(c)) {
                    number.append(c);
                    tf = true;
                } else head.append(c);

            }
            list.add(new Vertex(i, head.toString(), number.toString(), tail.toString()));
        }
        Collections.sort(list);
        answer = list.stream().map(vertex -> vertex.toString()).toArray(String[]::new);

        return answer;
    }

    class Vertex implements Comparable<Vertex> {
        int idx;
        String head;
        String number;
        String tail;

        public Vertex(int idx, String head, String number, String tail) {
            this.idx = idx;
            this.head = head;
            this.number = number;
            this.tail = tail;
        }

        @Override
        public int compareTo(Vertex o) {
            if (this.head.equalsIgnoreCase(o.head)) {
                if (this.number == o.number) return this.idx - o.idx;
                return Integer.parseInt(this.number) - Integer.parseInt(o.number);
            }
            return this.head.compareToIgnoreCase(o.head);
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            return sb.append(head).append(number).append(tail).toString();
        }
    }
}