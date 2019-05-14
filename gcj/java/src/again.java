import java.util.ArrayList;

// Sample input 1, in Java.
public class again {
	public again() {
	}
	
	static ArrayList<Integer> a = util.randInts((int) GetN(), 1, 5);
	static ArrayList<Integer> b = util.randInts((int) GetN(), 1, 5);
	
	static {
		util.pln(util.tos(a));
		util.pln(util.tos(b));
	}
	
	public static long GetN() {
		return 2L;
	}
	
	public static long GetA(long i) {
		return a.get((int) i);
		
	}
	
	public static long GetB(long i) {
		return b.get((int) i);
		
	}
}