 import java.util.Scanner;

 public class Q3{

    public static void main(String[] args) {
        int a=44;
        int b;
        b=a%10;
        
        if (b==4) {
            System.out.println("Last Digit is 4");
            if(a%3==0){
                System.out.println("divisible by 3");
            }
            else{
                System.out.println("not divisible by 3");
            }
        }
        else{
            System.out.println("Last digit is not 4");
        }
    }
}