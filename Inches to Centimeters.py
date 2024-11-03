import java.util.Scanner;

public class InchesToCentimeters {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int heightInInches = scanner.nextInt();
        double heightInCm = heightInInches * 2.54;
        System.out.printf("%.2f", heightInCm);
    }
}