import java.util.*;
public class VolumeOfSphere
{
    public static void main(String args[]) {
        Scanner sc=new Scanner(System.in);
        int r=sc.nextInt();
        double volume=1.333333*3.14*(r*r*r);
        System.out.printf("%.2f",volume);
    }
}