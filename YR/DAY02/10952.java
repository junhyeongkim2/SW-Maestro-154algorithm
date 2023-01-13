import java.util.*;

public class Main {

	public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
                
        while (scan.hasNextInt()) {
        	int A = scan.nextInt();
        	int B = scan.nextInt();
        	
        	if(A == 0 & B == 0) {
        		break;
        	}
          
          // 0 0 이 입력될 때에는 계산값이 나오면 안된다.
          System.out.println(A + B);
        }
	}
}
