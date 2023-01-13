package DAY5;
import java.io.*;
import java.util.*;

public class BOJ_10989 {
    public static void main(String[] args) throws IOException{
        /*List<Integer> list = new ArrayList<>(); -> 메모리 초과!
        counting Sort 방식 사용 -> 메모리 초과!
        Arrays.sort()사용 */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = Integer.parseInt(br.readLine());
        int[] array = new int[total];
        StringBuilder sb = new StringBuilder();


        for(int i = 0; i < total; i++)
        {
            array[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(array);

        for(int i = 0; i < total; i++){
            sb.append(array[i]).append("\n");
        }
        System.out.println(sb);
    }
}
