import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    
    int N = s.nextInt();
    
    for(int i = 0; i < N; i++) {
      for(int j = N; j > i + 1; j--) {
        System.out.print(" ");
      }
      for(int j = 0; j < (2 * i + 1); j++) {
        System.out.print("*");
      }
      System.out.println();
    }
  }
}
