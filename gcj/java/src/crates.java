// Sample input 1, in Java.
public class crates {
  public crates() {
  }

  public static long GetNumStacks() {
    return 3L;
  }

  public static long GetStackHeight(long i) {
    switch ((int)i) {
      case 1: return 2L;
      case 2: return 2L;
      case 3: return 4L;
      default: throw new IllegalArgumentException("Invalid argument");
    }
  }
}