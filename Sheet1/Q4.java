 class div {
    public static void main(String[] args) {
        int a=27;
        int b;
        b=a%10;
        
        if (a%7==0) {
            System.out.println("Number is divisible by 7");
            if (b==4){
                System.out.println("Last digit is 4");
            }
            else{
                System.out.println("Last digit is not 4");
                System.out.println("Number ib not divisible by 7");
            }
        }
        else{
            System.out.println("Number ib not divisible by 7");
        }
    }
}