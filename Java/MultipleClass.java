class Circle{
	double x,y;
	double r;
	double circumference(){
		return 2*3.14159*r;
	}
	double area(){
		return (22/7)*r*r;
	}
}
//Another Class Declaration
 class Box{
	 double width;
	 double height;
	 double depth;
	 double area(){
		 double a;
		 a=(width*height+height*depth+depth*width)*2;
		 return a;
	 }
	 double volume(){
		 double vol;
		 vol=width*height*depth;
		 return vol;
	 }
 }
 
 //declaring objects of type Circle and Box
 
 class MultipleClass{
	 public static void main(String args[]){
		 Circle c=new Circle();
		 Box b=new Box();
		 //Initializing the Circle
		 c.x=3.0;
		 c.y=4.0;
		 c.r=5.0;
		 //Initializing the Box
		  b.width=3.0;
		  b.height=4.0;
		  b.depth=5.0;
		  System.out.println("Circumference of circle" +c.circumference());
		  System.out.println("Area of Circle" +c.area());
		  System.out.println("Area of The Box" +b.area());
		  System.out.println("Volume of the Box" +b.volume());
	 }
 }
