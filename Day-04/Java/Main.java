import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        List<Board> bingos = new ArrayList<Board>();
        List<Integer> seq = new ArrayList<Integer>();

        String[] line = sc.nextLine().split(",");
        for (String k : line) {
            seq.add(Integer.parseInt(k));
        }

        while (sc.hasNext()) {
            int[][] matrix = new int[5][5];
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    matrix[i][j] = sc.nextInt();
                }
            }
            bingos.add(new Board(matrix));
        }

        int numNoBingos = 0;
        boolean part1Done = false;
        for (int k : seq) {
            for (Board b : bingos) {
                b.mark(k);
                if (b.checkBingo()) {
                    if (!part1Done) {
                        System.out.println("Part 1: " + k * b.sum());
                        part1Done = true;
                    }
                    if (numNoBingos == 1) {
                        System.out.println("Part 2: " + k * b.sum());
                        System.exit(0);
                    }
                }
            }
            numNoBingos = 0;
            List<Board> newBingos = new ArrayList<Board>();
            for (Board b : bingos) {
                if (!b.checkBingo()) {
                    numNoBingos++;
                    newBingos.add(b);
                }
            }
            bingos = newBingos;
        }
    }
}