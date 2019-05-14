// Sample input 3, in Java.
public class weird_editor {
	public weird_editor() {
	}
	
	public static long GetNumberLength() {
		return 10L;
	}
	
	public static long GetDigit(long i) {
		switch ((int) i) {
			case 0:
				return 4L;
			case 1:
				return 4L;
			case 2:
				return 3L;
			case 3:
				return 3L;
			case 4:
				return 2L;
			case 5:
				return 1L;
			case 6:
				return 0L;
			case 7:
				return 0L;
			case 8:
				return 0L;
			case 9:
				return 9L;
			default:
				throw new IllegalArgumentException("Invalid argument");
		}
	}
}