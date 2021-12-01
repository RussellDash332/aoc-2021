import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        List<Integer> m = new ArrayList<Integer>();
        while (sc.hasNext()) {
            m.add(sc.nextInt());
        }

        // Part 1
        int ans1 = 0;
        for (int i = 1; i < m.size(); i++) {
            if (m.get(i) > m.get(i - 1)) {
                ans1++;
            }
        }
        System.out.println("Part 1: " + ans1);

        // Part 2
        int ans2 = 0;
        for (int i = 3; i < m.size(); i++) {
            if (m.get(i) > m.get(i - 3)) {
                ans2++;
            }
        }
        System.out.println("Part 2: " + ans2);
    }
}
