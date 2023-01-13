import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int T = scan.nextInt();
		
		for(int i = 0; i < T; i++) {
			int A = scan.nextInt();
			int B = scan.nextInt();
			int C = A + B;
			
      // Case #x: A + B = C
			System.out.println("Case #" + (i + 1) + ": " + A + " + " + B + " = " + C);
		}
	}

}
