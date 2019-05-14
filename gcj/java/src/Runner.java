import java.util.ArrayList;

public class Runner {
	public static void main(final String[] args) {
		System.out.println("my-runner starts...");
		message.init();
		ArrayList<Thread> threads = new ArrayList<>();
		for (int i = 0; i < message.NumberOfNodes(); i++) {
			Thread thread = new Thread(new Runnable() {
				@Override
				public void run() {
					message.initThread();
					Main.main(args);
				}
			});
			thread.start();
			threads.add(thread);
		}
		for (Thread thread : threads) {
			try {
				thread.join();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		System.out.println("my-runner quit.");
	}
}
