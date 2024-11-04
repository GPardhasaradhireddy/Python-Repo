import java.util.*;
public class Hypotenuse
{
    public static void main(String args[]) {
        Scanner sc =new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        double c=(a*a)+(b*b);
        System.out.printf("%.2f",Math.sqrt(c));
    }
}