// Sample input 3, in Java.
public class gas_stations {
  public gas_stations() {
  }

  public static long GetNumKms() {
    return 3L;
  }

  public static long GetTankSize() {
    return 1L;
  }

  public static long GetGasPrice(long i) {
    switch ((int)i) {
      case 0: return 5L;
      case 1: return 1L;
      case 2: return 5L;
      default: throw new IllegalArgumentException("Invalid argument");
    }
  }
}