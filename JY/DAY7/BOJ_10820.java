package DAY7;

import java.io.*;

public class BOJ_10820 {
    public static void main(String[] arg) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringBuilder sb = new StringBuilder();

        while(str != null)
        {
            int small = 0;
            int big = 0;
            int num = 0;
            int blank = 0;
            for(int i = 0; i < str.length(); i++)
            {

                if(str.charAt(i) >= 'a' && str.charAt(i) <= 'z')small++;
                else if(str.charAt(i) >= 'A' && str.charAt(i) <= 'Z')big++;
                else if(str.charAt(i) >= '0' && str.charAt(i) <= '9')num++;
                else blank++;
            }
            System.out.println(sb.append(small).append(" ").append(big).append(" ").append(num).append(" ").append(blank));
            sb.setLength(0);
            str = br.readLine();
        }
    }

}
