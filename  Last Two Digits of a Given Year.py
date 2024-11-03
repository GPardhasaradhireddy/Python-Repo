import java.util.Scanner;

public class LastTwoDigits {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int year = scanner.nextInt();
        
        // Calculate the last two digits
        int lastTwoDigits = year % 100;
        
        // Print the last two digits, formatted to two digits
        System.out.printf("%02d\n", lastTwoDigits);
    }
}