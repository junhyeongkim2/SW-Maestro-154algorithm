import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        // T: 케이스 갯수
        int T, A, B;
        
        T = scan.nextInt();
        
        for(int i = 0; i<T; i++) {
            A = scan.nextInt();
            B = scan.nextInt();
            
            System.out.println(A + B);
        }
    }
}
