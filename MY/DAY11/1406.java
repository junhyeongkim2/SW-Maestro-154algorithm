/*
 * @author Minyeong Park
 * @date 2023.02.26.
 * 에디터
 * 시간초과 해결 방법 참고 : https://minhamina.tistory.com/17, https://mygumi.tistory.com/62, https://minhamina.tistory.com/18
 * 문제 링크 : https://www.acmicpc.net/problem/1406
 */



import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        LinkedList<Character> list = new LinkedList<Character>();
        for (int i = 0; i < str.length(); i++) {
            list.add(str.charAt(i));
        }

        ListIterator<Character> iter = list.listIterator();
        // 처음 커서는 문장의 맨 뒤에 있어야 하므로 커서를 맨 뒤로 이동시킴
        while (iter.hasNext()) {
            iter.next();
        }

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String command = br.readLine();
            char s = command.charAt(0);
            switch (s) {
                case 'L':
                    if (iter.hasPrevious()) {
                        iter.previous();
                    }
                    break;
                case 'D':
                    if (iter.hasNext()) {
                        iter.next();
                    }
                    break;
                case 'B':
                    if (iter.hasPrevious()) {
                        iter.previous();
                        iter.remove(); // next()나 previous() 메소드에 의해 반환된 가장 마지막 요소를 리스트에서 제거
                    }
                    break;
                case 'P':
                    char add_str = command.charAt(2);
                    iter.add(add_str);
                    break;
                default:
                    break;
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (Character chr : list) {
            bw.write(chr);
        }
        bw.flush();
        bw.close();
    }
}