import java.util.*;
// import java.util.stream.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        List<String> bits = new ArrayList<String>();
        List<String> bits2 = new ArrayList<String>();

        while (sc.hasNext()) {
            String bit = sc.nextLine();
            bits.add(bit);
            bits2.add(bit);
        }

        // Part 1
        int m = bits.size();
        int n = bits.get(0).length();
        int[] tmp = new int[n];
        for (int i = 0; i < m; i++) {
            String b = bits.get(i);
            for (int j = 0; j < n; j++) {
                tmp[j] += (int) b.charAt(j) - 48;
            }
        }
        int[] gam = new int[n];
        int[] eps = new int[n];
        for (int i = 0; i < n; i++) {
            gam[i] = 2 * tmp[i] > m ? 1 : 0;
            eps[i] = 2 * tmp[i] < m ? 1 : 0;
        }
        System.out.println("Part 1: " + binaryToDecimal(gam) * binaryToDecimal(eps));
    
        // Part 2
        for (int i = 0; i < n; i++) {
            if (bits.size() == 1) {
                break;
            }
            int[] freq = new int[2];
            for (String bit : bits) {
                freq[(int) bit.charAt(i) - 48] += 1;
            }
            if (freq[0] > freq[1]) {
                // bits = bits.stream().filter(x -> x.charAt(i) == '0').collect(Collectors.toList());
                List<String> newBits = new ArrayList<String>();
                for (String bt : bits) {
                    if (bt.charAt(i) == '0') {
                        newBits.add(bt);
                    }
                }
                bits = newBits;
            } else {
                // bits = bits.stream().filter(x -> x.charAt(i) == '1').collect(Collectors.toList());
                List<String> newBits = new ArrayList<String>();
                for (String bt : bits) {
                    if (bt.charAt(i) == '1') {
                        newBits.add(bt);
                    }
                }
                bits = newBits;
            }
        }
        for (int i = 0; i < n; i++) {
            if (bits2.size() == 1) {
                break;
            }
            int[] freq2 = new int[2];
            for (String bit : bits2) {
                freq2[(int) bit.charAt(i) - 48] += 1;
            }
            if (freq2[0] > freq2[1]) {
                // bits2 = bits2.stream().filter(x -> x.charAt(i) == '1').collect(Collectors.toList());
                List<String> newBits2 = new ArrayList<String>();
                for (String bt : bits2) {
                    if (bt.charAt(i) == '1') {
                        newBits2.add(bt);
                    }
                }
                bits2 = newBits2;
            } else {
                // bits2 = bits2.stream().filter(x -> x.charAt(i) == '0').collect(Collectors.toList());
                List<String> newBits2 = new ArrayList<String>();
                for (String bt : bits2) {
                    if (bt.charAt(i) == '0') {
                        newBits2.add(bt);
                    }
                }
                bits2 = newBits2;
            }
        }
        System.out.println("Part 2: " + binaryToDecimal(bits.get(0)) * binaryToDecimal(bits2.get(0)));
    }

    static int binaryToDecimal(int[] b) {
        int res = 0;
        for (int i : b) {
            res *= 2;
            res += i;
        }
        return res;
    }

    static int binaryToDecimal(String b) {
        int res = 0;
        for (int i = 0; i < b.length(); i++) {
            res *= 2;
            res += (int) b.charAt(i) - 48;
        }
        return res;
    }
}