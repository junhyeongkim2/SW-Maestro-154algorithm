import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int x = scan.nextInt();
		int y = scan.nextInt();
		
    // x, y 를 입력 받으면 해당되는 날짜 불러오기
		LocalDate date = LocalDate.of(2007, x, y);
    
    // 요일을 구하는 객체
		DayOfWeek dayOfWeek = date.getDayOfWeek();
    
    // 요일 구하기
    // 1 = 월, 2 = 화, 3 = 수, 4 = 목, 5 = 금, 6 = 토, 7 = 일
		int dayOfWeekNumber = dayOfWeek.getValue();
		
		switch(dayOfWeekNumber) {
		case 1:
			System.out.println("MON");
			break;
		case 2:
			System.out.println("TUE");			
			break;
		case 3:
			System.out.println("WED");			
			break;
		case 4:
			System.out.println("THU");			
			break;
		case 5:
			System.out.println("FRI");			
			break;
		case 6:
			System.out.println("SAT");			
			break;
		default:
			System.out.println("SUN");			
			break;
		}
	}
}
