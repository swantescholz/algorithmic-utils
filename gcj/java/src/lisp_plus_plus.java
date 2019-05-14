import java.util.ArrayList;

// Sample input 2, in Java.
public class lisp_plus_plus {
	public lisp_plus_plus() {
	}
	
	static {
//		util.seedRand(0);
	}
	
	static ArrayList<Integer> a = util.randInts(4, 1,2);
	
	static {
		util.pln(util.tos(a));
	}
	
	public static long GetLength() {return a.size();}
	
	public static char GetCharacter(long i) {
		if (1==a.get((int)i)) {
			return '(';
		}
		return ')';
		
	}
}