import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int[] month = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int day = y;
        for (int i = 0; i < x - 1; i++) {
            day += month[i];
        }

        String[] week = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};

        System.out.println(week[day % 7]);
    }
}