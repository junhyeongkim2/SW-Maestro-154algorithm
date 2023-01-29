import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        int N = s.nextInt();
        
        /*
        *        *
        **      **
        ***    ***
        ****  ****
        **********
        */
      
        // 1 ~ N 줄 반복
        for(int i = 0; i < N; i++) {
          
            // 왼쪽에서 증가하는 * 작성
            for(int j = 0; j < i + 1; j++) {
                System.out.print("*");
            }
          
            // * 사이에 있는 "  " 작성. 2배씩 늘어나므로 "  "로 작성했다.
            for(int j = N; j > i + 1; j--) {
                System.out.print("  ");
            }
          
            // 오른쪽에서 증가하는 * 작성
            for(int j = 0; j < i + 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
      
        /*
        ****  ****
        ***    ***
        **      **
        *        *
        */
      
        // N ~ (2 * N - 1) 줄 반복
        for(int i = 0; i < N; i++) {
          
            // 왼쪽에서 감소하는 * 작성
            for(int j = N; j > i + 1; j--) {
                System.out.print("*");
            }
          
            // * 사이에 있는 "  " 작성
            for(int j = 0; j < i + 1; j++) {
                System.out.print("  ");
            }
          
            // 오른쪽에서 감소하는 * 
            for(int j = N; j > i + 1; j--) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
