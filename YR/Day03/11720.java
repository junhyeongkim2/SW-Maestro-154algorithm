import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    
    int N = scan.nextInt();
    
    // 일단 String 으로 모든 수를 받는다
    String number = scan.next();
    
    int sum = 0;
    
    for(int i = 0; i < N; i++) {
      // charAt(i) 로 입력된 수를 나눠서 sum 에 저장한다
      sum += number.charAt(i) - 48;
    }
    System.out.println(sum);
  }
}
