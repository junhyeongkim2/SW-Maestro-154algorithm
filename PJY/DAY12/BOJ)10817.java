import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for(int i = 0; i < 3; i++){
            pq.add(sc.nextInt());
        }
        pq.poll();
        System.out.println(pq.poll());

        sc.close();
    }
}