import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class util {
	
	public static void goo() {
		System.out.println("goo");
	}
	
	
	public static ArrayList<Integer> randInts(int count, int min, int max) {
		ArrayList<Integer> res = new ArrayList<>();
		for (int i = 0; i < count; i++) {
			res.add(rand.nextInt(max-min+1) + min);
		}
		return res;
	}
	
	private static Random rand = new Random();
	
	public static void seedRand(long seed) {
		rand.setSeed(seed);
	}
	
	public static ArrayList<Long> randLongs(int count, long min, long max) {
		ThreadLocalRandom rand = ThreadLocalRandom.current();
		ArrayList<Long> res = new ArrayList<>();
		for (int i = 0; i < count; i++) {
			res.add(rand.nextLong(min, max + 1));
		}
		return res;
	}
	
	public static ArrayList<Float> randFloats(int count, float min, float max) {
		ArrayList<Float> res = new ArrayList<>();
		for (int i = 0; i < count; i++) {
			res.add(min + rand.nextFloat()*(max-min));
		}
		return res;
	}
	
	public static ArrayList<Double> randDoubles(int count, double min, double max) {
		ArrayList<Double> res = new ArrayList<>();
		for (int i = 0; i < count; i++) {
			res.add(min + rand.nextDouble()*(max-min));
		}
		return res;
	}
	
	public static void pln(Object... objs) {
		StringBuilder sb = new StringBuilder();
		for (Object obj : objs) {
			sb.append(" ").append(obj.toString());
		}
		if (sb.length()==0) {
			System.out.println();
			return;
		}
		String res = sb.toString().substring(1);
		System.out.println(res);
	}
	
	public static <T> String tos(Iterable<T> list) {
		StringBuilder sb = new StringBuilder();
		for (Object obj : list) {
			sb.append(", ").append(obj.toString());
		}
		if (sb.length()==0) {
			return "[]";
		}
		String res = "[" + sb.toString().substring(2) + "]";
		return res;
	}
	
	public static <T> String tos(T[] list) {
		StringBuilder sb = new StringBuilder();
		for (Object obj : list) {
			sb.append(", ").append(obj.toString());
		}
		if (sb.length()==0) {
			return "[]";
		}
		String res = "[" + sb.toString().substring(2) + "]";
		return res;
	}
	
	public static void main(String[] args) {
		List<Integer> a = randInts(15,3,9);
		pln(a);
	}
}
