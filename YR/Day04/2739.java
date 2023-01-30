import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int N = scan.nextInt();
		
		for(int i = 0; i < 9; i++) {
      
			int result = N * (i + 1);
      
			// N * (i + 1) = result
			System.out.println(N + " * " + (i + 1) + " = "+ result);
		}
	}
}
