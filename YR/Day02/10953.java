import java.util.*;

public class Main {

	public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int T = scan.nextInt();
        
        for(int i = 0; i < T; i++) {
        	String str = scan.next();
            
        	String[] split = str.split(",");
            
        	int A = Integer.parseInt(split[0]);
        	int B = Integer.parseInt(split[1]);
            
        	System.out.println(A + B);
        	
        }
        
	}

}
