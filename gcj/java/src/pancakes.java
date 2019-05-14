// Sample input 1, in Java.
public class pancakes {
	public pancakes() {
	}
	
	public static long GetStackSize() {
		return 4L;
	}
	
	public static long GetNumDiners() {
		return 4L;
	}
	
	public static long GetStackItem(long i) {
		switch ((int) i) {
			case 0:
				return 3L;
			case 1:
				return 1L;
			case 2:
				return 2L;
			case 3:
				return 0L;
			default:
				throw new IllegalArgumentException("Invalid argument");
		}
	}
}