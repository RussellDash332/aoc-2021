public class Board {
    public int[][] matrix;

    Board(int[][] mat) {
        this.matrix = mat;
    }

    void mark(int val) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (this.matrix[i][j] == val) {
                    this.matrix[i][j] = 0;
                }
            }
        }
    }

    int sum() {
        int ans = 0;
        for (int[] r : this.matrix) {
            for (int v : r) {
                ans += v;
            }
        }
        return ans;
    }

    boolean checkBingo() {
        int sr = 0;
        int sd = 0;
        int srd = 0;
        int sc = 0;
        for (int i = 0; i < 5; i++) {
            sd += this.matrix[i][i];
            srd += this.matrix[i][4-i];
            sc = 0;
            sr = 0;
            for (int j = 0; j < 5; j++) {
                sc += this.matrix[j][i];
                sr += this.matrix[i][j];
            }
            if (sc == 0 || sr == 0) {
                return true;
            }
        }
        return (sd == 0 || srd == 0);
    }

    void print() {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(this.matrix[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}