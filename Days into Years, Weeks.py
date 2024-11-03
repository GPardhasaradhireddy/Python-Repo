import java.util.Scanner;

public class DaysToYearsWeeks {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int D = scanner.nextInt();
        
        int years = D / 365;
        int weeks = (D % 365) / 7;
        
        System.out.println(years);
        System.out.println(weeks);
    }
}