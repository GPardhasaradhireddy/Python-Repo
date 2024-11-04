import java.util.Scanner;

public class KmphToMps {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int k = scanner.nextInt();
        double m = k / 3.6;
        System.out.printf("%.2f", m);
}
}