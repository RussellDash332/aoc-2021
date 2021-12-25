class Pair {
    int row;
    int col;

    Pair(int row, int col) {
        this.row = row;
        this.col = col;
    }

    @Override
    public boolean equals(Object o) {
        if (o == this) {
            return true;
        } else if (o instanceof Pair) {
            Pair o2 = (Pair) o;
            return o2.row == this.row && o2.col == this.col;
        } else {
            return false;
        }
    }

    @Override
    public int hashCode() {
        return 1000 * this.row + this.col;
    }

    @Override
    public String toString() {
        return this.row+"-"+this.col;
    }
}