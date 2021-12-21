import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        long[] arr = new long[9];
        String[] line = sc.nextLine().split(",");

        for (String i : line) {
            arr[Integer.parseInt(i)]++;
        }

        for (int i = 0; i < 256; i++) {
            long[] newArr = new long[9];
            for (int j = 0; j < 9; j++) {
                if (j == 0) {
                    newArr[6] += arr[0];
                    newArr[8] += arr[0];
                } else {
                    newArr[j - 1] += arr[j];
                }
            }
            arr = newArr;
            if (i == 79) {
                System.out.println("Part 1: " + sum(arr));
            }
        }
        System.out.println("Part 2: " + sum(arr));
    }

    static long sum(long[] arr) {
        long s = 0L;
        for (long i : arr) {
            s += i;
        }
        return s;
    }
}