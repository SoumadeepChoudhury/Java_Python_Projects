package soumadeep;

public class Calc {

	public static void main(String[] args) {
		geo(2, 4);
		geo(2.0);
		geo(2.0f);
	}

	static void geo(int r, int h) {
		double volume = 1.0 / 3 * 22.0 / 7 * r * r * h;
		System.out.println("Volume of cone: " + volume);
	}

	static void geo(double r) {
		double cir = 2 * 3.14 * r;
		System.out.println("Circumference of circle: " + cir);
	}

	static void geo(float r) {
		double area = 22.0 / 7 * r * r / 4;
		System.out.println("Area of sector: " + area);
	}

}
