package DAY1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.*;

public class BOJ10814 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<User> userList = new ArrayList<>();

        // set input
        int repeat = Integer.parseInt(br.readLine());
        for(int i = 0 ; i < repeat; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            User user = new User(Integer.parseInt(st.nextToken()), st.nextToken());
            userList.add(user);
        }

        // sort
        Collections.sort(userList, new Comparator<User>(){
            @Override
            public int compare(User o1, User o2){
                return o1.getAge() - o2.getAge();
            }
        });

        for(User user : userList)
            System.out.println(user.toString());
    }

    static class User{
        private int age;
        private String name;

        public int getAge() {
            return age;
        }

        public String getName() {
            return name;
        }

        public User(int age, String name) {
            this.age = age;
            this.name = name;
        }

        @Override
        public String toString(){
            return this.age + " " + this.name;
        }
    }
}


/*
User class 생성 후 Comparator 익명 클래스로 객체 생성 후에 Collection.sort() 매개변수에 집어넣어줬음
나이가 같을 때 가입한 사람이 앞에오는 경우는 고려안해주어도 됨 -> 가입한 사람이 뒤로 가는 경우는? 음수 리턴 (양수 리턴을 해주어야 하는 게 아닌가?)
 */