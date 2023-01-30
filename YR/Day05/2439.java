import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    
    int N = s.nextInt();
    
    for(int i = 0; i < N; i++) {
      
      // 한 줄의 " "의 갯수는 "*"의 갯수보다 많아야 한다.
      for(int j = N; j > i + 1; j--) {
        System.out.print(" ");
      }
      
      // "*"의 갯수는 1개씩 늘어나야 한다.
      for(int j = 0; j < i + 1; j++) {
        System.out.print("*");
      }
      System.out.println();
    }
  }
}
