import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        long x = 0;
        long y1 = 0;
        long y2 = 0;
        while (sc.hasNext()) {
            String cmd = sc.next();
            int d = sc.nextInt();
            switch (cmd) {
                case "forward":
                    x += d;
                    y2 += y1 * d;
                    break;
                case "up":
                    y1 -= d;
                    break;
                default:
                    y1 += d;
                    break;
            }
        }
        System.out.println("Part 1: " + (x * y1));
        System.out.println("Part 2: " + (x * y2));
    }
}
