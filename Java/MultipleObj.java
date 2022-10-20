class Circle{
	double x,y; //the Circumference of the center
	double r; //the radius
	
	//Methods that return circumference 
	double circumference(){
		return 2*3.14159*r;
	}
	//Method that return area
	double area(){
		return (22/7)*r*r;
	}
}
//Declaring object of the Circle class
class MultipleObj{
	public static void main(String args[]){
		Circle c1=new Circle();
		Circle c2=new Circle();
		//Initialize the circle
		
		c1.x=0.0;
		c1.y=3.0;
		c1.r=5.0;
		c2.x=7.0;
		c2.y=8.0;
		c2.r=4.0;
		System.out.println("Circumference circle1" +c1.circumference());
		System.out.println("Area circle1"+ c1.area());
		System.out.println("Circumference circle2" +c2.circumference());
		System.out.println("Area circle2"+ c2.area());
	}
}