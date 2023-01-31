import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    
    int N = s.nextInt();
    
    // 줄 반복
    for(int i = 0; i < N; i++) {
      
      // * 반복
      for(int j = 0; j < i + 1; j++) {
        
        System.out.print("*");
        
      }
      
      System.out.println();
    }
  }
}
