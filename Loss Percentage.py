import java.util.*;
public class LossPercentage{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        double x=sc.nextDouble();
        double y=sc.nextDouble();
        double l=((x-y)/x)*100;
        System.out.printf("%.2f",l);
        sc.close();
    }
}