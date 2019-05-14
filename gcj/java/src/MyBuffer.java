import java.util.ArrayDeque;
import java.util.ArrayList;

public class MyBuffer {
	private int maxSize;
	private ArrayDeque<Byte> bytes = new ArrayDeque<>();
	
	public MyBuffer(int maxSize) {
		this.maxSize = maxSize;
	}
	
	public int size() {
		return bytes.size();
	}
	
	public void putChar(char value) {
		bytes.addLast((byte) ((value&0xFF00)>>8));
		bytes.addLast((byte) (value&0x00FF));
		checkSize();
	}
	public void putInt(int value) {
		bytes.addLast((byte) ((value&0xFF000000)>>24));
		bytes.addLast((byte) ((value&0x00FF0000)>>16));
		bytes.addLast((byte) ((value&0x0000FF00)>>8));
		bytes.addLast((byte) (value&0x000000FF));
		checkSize();
	}
	public void putLong(long value) {
		bytes.addLast((byte) ((value&0xFF00000000000000L)>>56));
		bytes.addLast((byte) ((value&0x00FF000000000000L)>>48));
		bytes.addLast((byte) ((value&0x0000FF0000000000L)>>40));
		bytes.addLast((byte) ((value&0x000000FF00000000L)>>32));
		bytes.addLast((byte) ((value&0x00000000FF000000L)>>24));
		bytes.addLast((byte) ((value&0x0000000000FF0000L)>>16));
		bytes.addLast((byte) ((value&0x000000000000FF00L)>>8));
		bytes.addLast((byte) (value&0x00000000000000FFL));
		checkSize();
	}
	public char getChar() {
		if (bytes.size() < 2) {
			throw new RuntimeException("buffer contains no char");
		}
		char value = 0;
		for (int i = 0; i < 2; i++) {
			value = (char)((value << 8) + (bytes.pollFirst()));
		}
		return value;
	}
	public int getInt() {
		if (bytes.size() < 4) {
			throw new RuntimeException("buffer contains no int");
		}
		int value = 0;
		for (int i = 0; i < 4; i++) {
			value = (value << 8) + (bytes.pollFirst() & 0xff);
		}
		return value;
	}
	public long getLong() {
		if (bytes.size() < 8) {
			throw new RuntimeException("buffer contains no long");
		}
		long value = 0;
		for (int i = 0; i < 8; i++) {
			value = (value << 8) + (bytes.pollFirst() & 0xff);
		}
		return value;
	}
	public void addAll(MyBuffer other) {
		this.bytes.addAll(other.bytes);
		checkSize();
	}
	
	private void checkSize() {
		if (bytes.size() > maxSize) {
			throw new RuntimeException("buffer size exceeds max-size!");
		}
	}
}
