// Sample input 2, in Java.
public class asteroids {
  public asteroids() {
  }

  public static long GetHeight() {
    return 6L;
  }

  public static long GetWidth() {
    return 4L;
  }

  public static char GetPosition(long i, long j) {
    if (i == 5L && j == 0L) return '1';
    if (i == 5L && j == 1L) return '#';
    if (i == 5L && j == 2L) return '7';
    if (i == 5L && j == 3L) return '8';
    if (i == 4L && j == 0L) return '0';
    if (i == 4L && j == 1L) return '0';
    if (i == 4L && j == 2L) return '1';
    if (i == 4L && j == 3L) return '1';
    if (i == 3L && j == 0L) return '#';
    if (i == 3L && j == 1L) return '2';
    if (i == 3L && j == 2L) return '#';
    if (i == 3L && j == 3L) return '9';
    if (i == 2L && j == 0L) return '0';
    if (i == 2L && j == 1L) return '1';
    if (i == 2L && j == 2L) return '3';
    if (i == 2L && j == 3L) return '6';
    if (i == 1L && j == 0L) return '0';
    if (i == 1L && j == 1L) return '#';
    if (i == 1L && j == 2L) return '8';
    if (i == 1L && j == 3L) return '#';
    if (i == 0L && j == 0L) return '2';
    if (i == 0L && j == 1L) return '1';
    if (i == 0L && j == 2L) return '#';
    if (i == 0L && j == 3L) return '9';
    throw new IllegalArgumentException("Invalid argument");
  }
}