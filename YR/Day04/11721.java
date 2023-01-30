import java.util.*;

public class Main {
  public static void main (String[] args) {
    Scanner scan = new Scanner(System.in);
    
    String str = scan.next();
    
    // n = 0, 1, 2, ...
    int n = str.length() / 10;
    
    int index = 0;
    
    for(int i = 0; i < n; i++) {
      // 한 줄에 단어는 10개씩 끊어서 나와야 한다: (0, 10) (10, 20) (20, 30) ...
      String result1 = str.substring(index, (index + 10));
      
      System.out.println(result1);
      
      // 10개 단위로 반복되어야 한다
      index += 10;
    }
    
    // 마지막 줄에는 10개 미만의 글자가 나와야 한다
    // n = 1, 2, 3, ...
    n = str.length() % 10;
    String result2 = str.substring(str.length() - n);
    System.out.println(result2);
  }
}
