import java.util.Scanner;
public class Q8 {
    public static void main(String[] args) {
        int a;
        Scanner src = new Scanner(System.in);
        System.out.println("Enter Your Age");
        a = src.nextInt();      
        if (a>=18) {
            System.out.println("elogible to vote");
        }
        else{
            System.out.println("Not");
        }
    }
}