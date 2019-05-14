// Sample input 2, in Java.
public class todd_and_steven {
	public todd_and_steven() {
	}
	
	public static long GetToddLength() {
		return 1L;
	}
	
	public static long GetStevenLength() {
		return 1L;
	}
	
	public static long GetToddValue(long i) {
		switch ((int) i) {
			case 0:
				return 101L;
			default:
				throw new IllegalArgumentException("Invalid argument");
		}
	}
	
	public static long GetStevenValue(long i) {
		switch ((int) i) {
			case 0:
				return 100L;
			default:
				throw new IllegalArgumentException("Invalid argument");
		}
	}
}