import java.util.*;
import java.lang.*;
import java.io.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in); 
        
        int a = sc.nextInt();           
        int b = sc.nextInt();
        int c = sc.nextInt();
        
        int[] num = {a, b, c};      
        
        Arrays.sort(num);           //배열정렬
        
        System.out.println(num[1]); //두번째로 큰수
    } 
