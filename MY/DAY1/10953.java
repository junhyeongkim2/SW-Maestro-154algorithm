import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            String line = br.readLine();
            String[] ab = line.split(",");
            System.out.println(Integer.parseInt(ab[0]) + Integer.parseInt(ab[1]));
        }
    }
}