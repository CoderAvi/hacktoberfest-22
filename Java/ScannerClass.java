import java.util.Scanner;
class ScannerClass{
	public static void main(String args[]){
		//Scanner definition
		Scanner scn = new Scanner(System.in);
		//input is string read by nextline() function.
		String str = scn.nextLine();
		//print String
		System.out.println("Entered String:"+str);
		
		//input us an integer read by nextInt() function
		int x = scn.nextInt();
		
		//print integer 
		System.out.println("Entered integer:"+x);
		
		//input is floating value read by nextFloat() function
		float f = scn.nextFloat();
		
		//print floating value
		System.out.println("Entered FloatValue:"+f);
	}
}