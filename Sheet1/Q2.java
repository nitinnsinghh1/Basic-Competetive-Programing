import java.util.Scanner;

public class Q2 {
    public static void main(String[] args) {
        int a;
        Scanner src = new Scanner(System.in);
        System.out.println("Enter Your Number");
        a = src.nextInt();
               
        if (a%4==0) {
            System.out.println("Number is divisible by 7");
        }
        else{
            System.out.println("Number ib not divisible by 7");
        }
    }
}