import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    
    // N 개의 정수 입력 받음
    int N = s.nextInt();
    
    // N 개의 정수를 받을 배열 생성
    int[] number = new int[N];
    
    // N 개의 정수를 입력받고, 배열에 넣는다
    for(int i = 0; i < N; i++) {
      number[i] = s.nextInt();
    }
    
    // number 배열을 오름차순으로 정렬
    Arrays.sort(number);
    
    // number[0] = 최솟값
    // number[N - 1] = 최대값. N보다 배열의 크기가 1 작으므로 -1 처리한다. N 으로 입력할 경우 해당되는 숫자를 불러올 수 없다.
    System.out.print(number[0] + " " + number[N - 1]);
  }
}
