import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Map<Pair, Integer> m = new HashMap<Pair, Integer>();
        int row = 0;
        int col = 0;
        while (sc.hasNext()) {
            String line = sc.nextLine();
            if (col == 0) {
                col = line.length();
            }
            for (int c = 0; c < line.length(); c++) {
                if (line.charAt(c) != '.') {
                    m.put(new Pair(row, c), line.charAt(c) == '>' ? 1 : 2);
                }
            }
            row++;
    }

        boolean noChange = false;
        int ctr = 0;
        while (!noChange) {
            noChange = true;
            Map<Pair, Integer> m1 = new HashMap<Pair, Integer>();
            Map<Pair, Integer> m2 = new HashMap<Pair, Integer>();
            
            for (Pair p : m.keySet()) {
                if (m.get(p) == 1) {
                    if (m.get(new Pair(p.row, (p.col + 1) % col)) == null) {
                        noChange = false;
                        m1.put(new Pair(p.row, (p.col + 1) % col), 1);
                    } else {
                        m1.put(p, 1);
                    }
                } else {
                    m1.put(p, 2);
                }
            }

            for (Pair p : m1.keySet()) {
                if (m1.get(p) == 2) {
                    if (m1.get(new Pair((p.row + 1) % row, p.col)) == null) {
                        noChange = false;
                        m2.put(new Pair((p.row + 1) % row, p.col), 2);
                    } else {
                        m2.put(p, 2);
                    }
                } else {
                    m2.put(p, 1);
                }
            }
            
            m = m2;
            ctr++;
        }

        System.out.println("Part 1: " + ctr);
        System.out.println("Part 2: THE END!");
    }
}
