import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[5];
        int num = 0;

        for(int i = 0; i<5; i++){
            int k = sc.nextInt();
            arr[i] = k;
            num += k;
        }

        Arrays.sort(arr);
        System.out.println(num/5);
        System.out.println(arr[2]);

		sc.close();
	}
}
