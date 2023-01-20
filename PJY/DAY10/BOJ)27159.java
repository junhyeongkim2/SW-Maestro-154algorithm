import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int result = 0;

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
            result += validatedResult(arr, i);
        }

        System.out.println(result);

        sc.close();
    }

    public static int validatedResult(int[] arr, int n){
        if(n == 0) return arr[n];
        if(arr[n-1]+1 == arr[n]) return 0;
        return arr[n];
    }
}