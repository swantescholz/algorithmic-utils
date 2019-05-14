public class Foo {
	public static void main(String[] args) {
		System.out.println("foo");
		MyBuffer b = new MyBuffer(300);
		b.putChar('x');
		b.putChar('y');
		System.out.println(b.getChar());
		System.out.println(b.getChar());
		for (long i = 1000000000000L; i < 1000000000006L; i++) {
			b.putLong(i);
		}
		System.out.println(b.getLong());
		System.out.println(b.getLong());
	}
}
