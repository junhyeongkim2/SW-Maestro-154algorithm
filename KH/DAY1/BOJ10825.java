package DAY1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ10825 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Student> studentList = new ArrayList<>();

        // set input
        int repeat = Integer.parseInt(br.readLine());
        for (int i = 0; i < repeat; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int korean = Integer.parseInt(st.nextToken());
            int english = Integer.parseInt(st.nextToken());
            int math = Integer.parseInt(st.nextToken());
            Student student = new Student(name, korean, english, math);
            studentList.add(student);
        }

        Collections.sort(studentList, new Comparator<Student>() {
            @Override
            public int compare(Student o1, Student o2) {
                // 모든 점수 같으면 이름 사전 순 정렬
                if (o1.scoreEquals(o2))
                    return o1.getName().compareTo(o2.getName());

                // 국어 점수와 영어 점수 같으면 수학 점수 내림차순
                if (o1.getKoreanScore() == o2.getKoreanScore() && o1.getEnglishScore() == o2.getEnglishScore())
                    return o2.getMathScore() - o1.getMathScore();

                // 국어 점수가 같으면 영어 점수 오름차순
                if(o1.getKoreanScore() == o2.getKoreanScore())
                    return o1.getEnglishScore() - o2.getEnglishScore();

                return o2.getKoreanScore() - o1.getKoreanScore();
            }
        });

        for(Student student : studentList)
            System.out.println(student.getName());

    }

    static class Student {
        private String name;
        private int koreanScore;
        private int englishScore;
        private int mathScore;

        public Student(String name, int koreanScore, int englishScore, int mathScore) {
            this.name = name;
            this.koreanScore = koreanScore;
            this.englishScore = englishScore;
            this.mathScore = mathScore;
        }

        public String getName() {
            return name;
        }

        public int getKoreanScore() {
            return koreanScore;
        }

        public int getEnglishScore() {
            return englishScore;
        }

        public int getMathScore() {
            return mathScore;
        }

        public boolean scoreEquals(Student student) {
            boolean answer = false;
            if (student.getEnglishScore() == this.getEnglishScore() && student.getKoreanScore() == this.getKoreanScore() && student.getMathScore() == this.getMathScore())
                answer = true;
            return answer;
        }
    }
}
