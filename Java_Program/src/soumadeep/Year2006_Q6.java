package soumadeep;

public class Year2006_Q6 {

	public static void main(String[] args) {
		String s = "January 26 is celebrated as the Republic Day of India.";
		s = s.replace("January", "August");
		s = s.replace("26", "15");
		s = s.replace("Republic", "Independence");
		System.out.print(s);
	}

}
