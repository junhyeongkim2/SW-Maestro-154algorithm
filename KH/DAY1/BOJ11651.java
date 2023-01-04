package DAY1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.*;

public class BOJ11650 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Location> locationList = new ArrayList<>();

        int repeat = Integer.parseInt(br.readLine());
        for(int i = 0 ; i < repeat; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            Location location = new Location(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            locationList.add(location);
        }

        // sort
        Collections.sort(locationList, new Comparator<Location>(){
            @Override
            public int compare(Location o1, Location o2){
                if(o1.getY() == o2.getY())
                    return o1.getX() - o2.getX();
                return o1.getY() - o2.getY();
            }
        });

        for(Location location : locationList)
            System.out.println(location.toString());
    }

    static class Location{
        private int x;
        private int y;

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public Location(int x, int y){
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString(){
            return x + " " + y;
        }
    }
}
