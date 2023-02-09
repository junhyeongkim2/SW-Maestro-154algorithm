import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String line;
        while ((line = br.readLine()) != null) {
            st = new StringTokenizer(line);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            System.out.println(a + b); // 처음에 StringBuilder로 만들어서 했는데 메모리 초과가 떴다. 잘 몰랐었는데, StringBuilder로 출력하는 방식이 꼭 좋은 것만은 아닌 것 같다.
        }
    }
}