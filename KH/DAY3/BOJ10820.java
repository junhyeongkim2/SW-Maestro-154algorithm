package DAY3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ10820 {
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;

        while((input = br.readLine()) != null){
            int lowerCaseCnt = 0;
            int upperCaseCnt = 0;
            int numberCnt = 0;
            int spaceCnt = 0;

            for(int i = 0 ; i < input.length(); i++){
                char ch = input.charAt(i);

                // 공백 검사
                if(ch == ' '){
                    spaceCnt++;
                    continue;
                }

                if(Character.isDigit(ch)){
                    numberCnt++;
                }else if(Character.isLowerCase(ch)){
                    lowerCaseCnt++;
                }else if(Character.isUpperCase(ch)){
                    upperCaseCnt++;
                }
            }
            sb.append(lowerCaseCnt).append(" ").append(upperCaseCnt).append(" ").append(numberCnt).append(" ").append(spaceCnt).append("\n");
        }
        System.out.println(sb.toString());
    }
}
