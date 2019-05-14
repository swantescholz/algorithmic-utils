import java.math.BigInteger;
import java.util.*;

class range implements Iterable<Integer> {
	public final int start; // inclusive
	public final int end; // exclusive
	
	public range(int end) {
		this.start = 0;
		this.end = end;
	}
	
	public range(int start, int end) {
		this.start = start;
		this.end = end;
	}
	
	public boolean isEmpty() {
		return end <= start;
	}
	
	public int size() {
		return end - start;
	}
	
	public range intersect(range other) {
		return new range(Math.max(start, other.start), Math.min(end, other.end));
	}
	
	public boolean contains(int i) {
		return i >= start && i < end;
	}
	
	// returns e.g. 5,16,3 -> [5,8],[8,12],[12,16]
	public range slice(int sliceIndex, int numSlices) {
		long d = size();
		int a = (int) ((sliceIndex * d) / numSlices);
		int b = (int) (((sliceIndex + 1) * d) / numSlices);
		return new range(a + start, b + start);
	}
	
	@Override
	public String toString() {
		return "(" + start + ", " + end + ")";
	}
	
	private class MyIterator implements Iterator<Integer> {
		
		private final range ab;
		private int current;
		
		public MyIterator(range ab) {
			this.ab = ab;
			this.current = ab.start;
		}
		
		@Override
		public boolean hasNext() {
			return current < ab.end;
		}
		
		@Override
		public Integer next() {
			return current++;
		}
		
		@Override
		public void remove() {
		}
	}
	
	@Override
	public Iterator<Integer> iterator() {
		return new MyIterator(this);
	}
}

class ipair implements Comparable<ipair> {
	
	public static ipair[] NESW4 = new ipair[]{new ipair(0, 1), new ipair(1, 0), new ipair(0, -1), new ipair(-1, 0)};
	public static ipair[] NESW8 = new ipair[]{
			new ipair(0, 1), new ipair(1, 1), new ipair(1, 0), new ipair(1, -1),
			new ipair(0, -1), new ipair(-1, -1), new ipair(-1, 0), new ipair(-1, 1)};
	
	public final int x;
	public final int y;
	
	public ipair(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	@Override
	public boolean equals(Object o) {
		if (this == o) return true;
		if (o == null || getClass() != o.getClass()) return false;
		
		ipair ipair = (ipair) o;
		
		if (x != ipair.x) return false;
		return y == ipair.y;
	}
	
	@Override
	public int hashCode() {
		int result = x;
		result = 31 * result + y;
		return result;
	}
	
	@Override
	public int compareTo(ipair other) {
		if (x < other.x) {
			return -1;
		}
		if (x > other.x) {
			return 1;
		}
		if (y < other.y) {
			return -1;
		}
		if (y > other.y) {
			return 1;
		}
		return 0;
	}
}

class Pair<A, B> {
	public final A a;
	public final B b;
	
	public Pair(A a, B b) {
		this.a = a;
		this.b = b;
	}
}

class misc {
	public static ArrayList<Integer> arange(int maxExclusive) {
		return arange(0, maxExclusive);
	}
	
	public static ArrayList<Integer> arange(int min, int maxExclusive) {
		ArrayList<Integer> res = new ArrayList<>();
		for (int i = min; i < maxExclusive; i++) {
			res.add(i);
		}
		return res;
	}
	
	// returns a list of chosen start values for this worker, and the remaining elements of the list also
	// null if worker should not work
	public static <T> Pair<ArrayList<T>, ArrayList<T>> splitListSubsets(ArrayList<T> list, int workerId,
	                                                                    int numWorkers) {
		int power2 = Integer.toBinaryString(numWorkers).length() - 1;
		if (power2 > list.size()) {
			power2 = list.size();
		}
		int numUsedWorkers = 1 << power2;
		if (workerId >= numUsedWorkers) {
			return null;
		}
		
		ArrayList<T> chosenElementsFromStart = new ArrayList<>();
		ArrayList<T> remainingElements = new ArrayList<>();
		for (int i = 0; i < power2; i++) {
			if (workerId % 2 == 1) {
				chosenElementsFromStart.add(list.get(i));
			}
			workerId /= 2;
		}
		for (int i = power2; i < list.size(); i++) {
			remainingElements.add(list.get(i));
		}
		return new Pair<ArrayList<T>, ArrayList<T>>(chosenElementsFromStart, remainingElements);
	}
	
	// returns fast sum(z**k for k in range(n+1)) % mod
	public static BigInteger constantGeometricSum(BigInteger z, BigInteger n, BigInteger mod) {
		BiMatrix m = new BiMatrix(2, 2);
		m.m[0][0] = z;
		m.m[0][1] = BigInteger.ZERO;
		m.m[1][0] = BigInteger.ONE;
		m.m[1][1] = BigInteger.ONE;
		m = m.modPow(n.add(BigInteger.ONE), mod);
		return m.m[1][0];
	}
	
	// returns fast sum(k*z**k for k in range(n+1)) % mod
	public static BigInteger linearGeometricSum(BigInteger z, BigInteger n, BigInteger mod) {
		BiMatrix m = new BiMatrix(3, 3);
		m.m[0][0] = z;
		m.m[0][1] = z;
		m.m[0][2] = z;
		m.m[1][0] = BigInteger.ZERO;
		m.m[1][1] = z;
		m.m[1][2] = z;
		m.m[2][0] = BigInteger.ZERO;
		m.m[2][1] = BigInteger.ZERO;
		m.m[2][2] = BigInteger.ONE;
		m = m.modPow(n, mod);
		return m.m[0][2];
	}
	
	public static ArrayList<Long> createSubsetSums(ArrayList<Long> list) {
		assert list.size() <= 27;
		ArrayList<Long> sums = new ArrayList<>();
		int size = list.size();
		int max = 1 << size;
		for (int subsetIndex = 0; subsetIndex < max; subsetIndex++) {
			int bits = subsetIndex;
			long sum = 0;
			for (int i = 0; i < size; i++) {
				if (bits % 2 == 0) {
					sum += list.get(i);
				}
				bits >>= 1;
			}
			sums.add(sum);
		}
		Collections.sort(sums);
		ArrayList<Long> res = new ArrayList<>();
		for (int i = 0; i < sums.size(); i++) {
			if (i == 0 || !Objects.equals(sums.get(i - 1), sums.get(i))) {
				res.add(sums.get(i));
			}
		}
		return res;
	}
	
	public static boolean subsetSumPossible(ArrayList<Long> list, long desiredSum) {
		ArrayList<Long> listA = new ArrayList<>();
		ArrayList<Long> listB = new ArrayList<>();
		for (int i = 0; i < list.size() / 2; i++) {
			listA.add(list.get(i));
		}
		for (int i = list.size() / 2; i < list.size(); i++) {
			listB.add(list.get(i));
		}
		ArrayList<Long> aSums = misc.createSubsetSums(listA);
		ArrayList<Long> bSums = misc.createSubsetSums(listB);
		int a = 0, b = bSums.size() - 1;
		while (true) {
			long sum = aSums.get(a) + bSums.get(b);
			if (sum < desiredSum) {
				a++;
				if (a >= aSums.size()) {
					break;
				}
			} else if (sum > desiredSum) {
				b--;
				if (b < 0) {
					break;
				}
			} else {
				return true;
			}
		}
		return false;
	}
}

class BiMatrix {
	final int h;
	final int w;
	final BigInteger[][] m;
	
	BiMatrix(int h, int w) {
		this.h = h;
		this.w = w;
		m = new BigInteger[h][w];
		for (int x = 0; x < w; x++) {
			for (int y = 0; y < h; y++) {
				if (x == y)
					m[y][x] = BigInteger.ONE;
				else
					m[y][x] = BigInteger.ZERO;
			}
		}
	}
	
	BiMatrix multiply(BiMatrix other) {
		BiMatrix res = new BiMatrix(this.h, other.w);
		for (int y = 0; y < h; y++) {
			for (int x = 0; x < other.w; x++) {
				BigInteger sum = BigInteger.ZERO;
				for (int i = 0; i < this.w; i++) {
					sum = sum.add(this.m[y][i].multiply(other.m[i][x]));
				}
				res.m[y][x] = sum;
			}
		}
		return res;
	}
	
	BiMatrix mod(BigInteger mod) {
		BiMatrix res = new BiMatrix(this.h, this.w);
		for (int y = 0; y < h; y++) {
			for (int x = 0; x < w; x++) {
				res.m[y][x] = this.m[y][x].mod(mod);
			}
		}
		return res;
	}
	
	BiMatrix modPow(BigInteger power, BigInteger mod) {
		BiMatrix x = new BiMatrix(h, w);
		ArrayList<Boolean> bits = new ArrayList<>();
		do {
			bits.add(Objects.equals(power.mod(BigInteger.valueOf(2)), BigInteger.ONE));
			power = power.shiftRight(1);
		} while (power.compareTo(BigInteger.ZERO) > 0);
		Collections.reverse(bits);
		for (Boolean bit : bits) {
			if (bit)
				x = ((x.multiply(x).mod(mod)).multiply(this)).mod(mod);
			else
				x = x.multiply(x).mod(mod);
		}
		return x.mod(mod);
	}
}

public class Main {
	static final String impossible = "IMPOSSIBLE";
	final int quit = Integer.MIN_VALUE, intmin = Integer.MIN_VALUE, intmax = Integer.MAX_VALUE;
	final long lquit = Long.MIN_VALUE, longmin = Long.MIN_VALUE, longmax = Long.MAX_VALUE;
	final int __numNodes = message.NumberOfNodes();
	final int numSlaves = __numNodes - 1;
	final int master = __numNodes - 1;
	final int id = message.MyNodeId();
	// ===================================
	long mod = 1000000007L;
	int nn = (int) weird_editor.GetNumberLength();
	
	void doSlave() {
		range ab = new range(nn).slice(id, numSlaves);
		
	}
	
	void doMaster() {
	
	}
	
	// ===================================
	public static void main(String[] args) {
		Main mainObj = new Main();
		if (mainObj.id == mainObj.master) {
			mainObj.doMaster();
		} else {
			mainObj.doSlave();
		}
	}
	
	
}