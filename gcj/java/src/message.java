import com.sun.org.apache.xpath.internal.SourceTree;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.locks.ReentrantLock;

// A program you submit to Distributed Code Jam will be compiled by Google, and
// will run on multiple computers (nodes). This library describes the interface
// needed for the nodes to identify themselves and to communicate.
//
// This is the version of the interface for programs written in Java. Your
// program doesn't need to import it and should always use a class name before
// accessing the static methods, e.g.:
// int n = message.NumberOfNodes();
public class message {
	private static int NUMBER_OF_NODES = 3;
	private static int MESSAGE_CAPACITY_IN_BYTES = 10000;
	
	private static HashMap<Long, Integer> threadId2nodeId = new HashMap<>();
	// source, target are the keys
	private static MyBuffer[][] outBuffers = null;
	private static ArrayList<ArrayList<ArrayDeque<MyBuffer>>> midBuffers = null;
	private static MyBuffer[][] inBuffers = null;
	private static CountDownLatch midLatches[][];
	private static CountDownLatch inLatches[];
	private static ReentrantLock[][] midLocks = null;
	private static ReentrantLock[] inLocks = null;
	private static int[] sendCounts = new int[NUMBER_OF_NODES];
	
	public static void init() {
		outBuffers = new MyBuffer[NUMBER_OF_NODES][NUMBER_OF_NODES];
		midBuffers = new ArrayList<>(NUMBER_OF_NODES);
		midLocks = new ReentrantLock[NUMBER_OF_NODES][NUMBER_OF_NODES];
		inLocks = new ReentrantLock[NUMBER_OF_NODES];
		inBuffers = new MyBuffer[NUMBER_OF_NODES][NUMBER_OF_NODES];
		midLatches = new CountDownLatch[NUMBER_OF_NODES][NUMBER_OF_NODES];
		inLatches = new CountDownLatch[NUMBER_OF_NODES];
		for (int x = 0; x < NUMBER_OF_NODES; x++) {
			ArrayList<ArrayDeque<MyBuffer>> midLine = new ArrayList<>(NUMBER_OF_NODES);
			for (int y = 0; y < NUMBER_OF_NODES; y++) {
				outBuffers[x][y] = new MyBuffer(MESSAGE_CAPACITY_IN_BYTES);
				midLatches[x][y] = new CountDownLatch(1);
				midLocks[x][y] = new ReentrantLock();
				midLine.add(new ArrayDeque<MyBuffer>());
			}
			inLatches[x] = new CountDownLatch(1);
			inLocks[x] = new ReentrantLock();
			midBuffers.add(midLine);
		}
	}
	
	public static synchronized void initThread() {
		long threadId = Thread.currentThread().getId();
		threadId2nodeId.put(threadId, threadId2nodeId.size());
	}
	
	public static int NumberOfNodes() {
		return NUMBER_OF_NODES;
	}
	
	public static int MyNodeId() {
		long threadId = Thread.currentThread().getId();
		return threadId2nodeId.get(threadId);
	}
	
	public static void Send(int target) {
		int myNodeId = MyNodeId();
		inLocks[target].lock();
		midLocks[myNodeId][target].lock();
		midBuffers.get(myNodeId).get(target).add(outBuffers[myNodeId][target]);
		outBuffers[myNodeId][target] = new MyBuffer(MESSAGE_CAPACITY_IN_BYTES);
		assert midLatches[myNodeId][target].getCount() == 1;
		midLatches[myNodeId][target].countDown();
		inLatches[target].countDown();
		inLocks[target].unlock();
		sendCounts[myNodeId] += 1;
		assert sendCounts[myNodeId] <= 1000 : "too many nodes (" + sendCounts[myNodeId] + " > 1000) sent from node " + myNodeId;
		midLocks[myNodeId][target].unlock();
	}
	
	public static int Receive(int source) {
		assert source >= -1;
		int myNodeId = MyNodeId();
		if (source == -1) {
			try {
				inLatches[myNodeId].await();
				inLocks[myNodeId].lock();
				inLatches[myNodeId] = new CountDownLatch(1);
				
				for (int i = 0; i < NUMBER_OF_NODES; i++) {
					if (midLatches[i][myNodeId].getCount() == 0) {
						if (source == -1) {
							source = i;
						} else {
							inLatches[myNodeId].countDown(); // other sending node found, so no wait for next time
							break;
						}
					}
				}
				if (midBuffers.get(source).get(myNodeId).size() > 1) {
					inLatches[myNodeId].countDown(); // more than one message there, so no wait for next time
				}
				inLocks[myNodeId].unlock();
				assert source != -1;
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		try {
			midLatches[source][myNodeId].await();
			midLocks[source][myNodeId].lock();
			inBuffers[source][myNodeId] = midBuffers.get(source).get(myNodeId).pollFirst();
			if (midBuffers.get(source).get(myNodeId).size() == 0) {
				midLatches[source][myNodeId] = new CountDownLatch(1);
			}
			midLocks[source][myNodeId].unlock();
		} catch (InterruptedException e) {
			e.printStackTrace();
			assert false;
		}
		return source;
	}
	
	private static void debug(String msg) {
		System.out.println(msg);
	}
	
	public static void PutChar(int target, char value) {
		debug("put " + MyNodeId() + " -> " + target + " : " + value);
		outBuffers[MyNodeId()][target].putChar(value);
	}
	
	public static void PutInt(int target, int value) {
		debug("put " + MyNodeId() + " -> " + target + " : " + value);
		outBuffers[MyNodeId()][target].putInt(value);
	}
	
	public static void PutLL(int target, long value) {
		debug("put " + MyNodeId() + " -> " + target + " : " + value);
		outBuffers[MyNodeId()][target].putLong(value);
	}
	
	public static char GetChar(int source) {
		char value = inBuffers[source][MyNodeId()].getChar();
//		debug("get " + source + " -> " + MyNodeId() + " : " + value);
		return value;
	}
	
	public static int GetInt(int source) {
		int value = inBuffers[source][MyNodeId()].getInt();
//		debug("get " + source + " -> " + MyNodeId() + " : " + value);
		return value;
	}
	
	public static long GetLL(int source) {
		long value = inBuffers[source][MyNodeId()].getLong();
//		debug("get " + source + " -> " + MyNodeId() + " : " + value);
		return value;
	}
	
}