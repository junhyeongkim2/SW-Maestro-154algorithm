import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int N = scan.nextInt();
        
        for(int i = N; i <= N; i--) {
            System.out.println(i);
            
            // i 를 지정하지 않으면, 음수 무한대로 된다.
            if(i == 1) {
                break;
            }
        }
    }
}
