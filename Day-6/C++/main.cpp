#include <bits/stdc++.h>
#include <vector>
using namespace std;

long sum(long arr[9]) {
    long s = 0;
    for (int i = 0; i < 9; i++) {
        s += arr[i];
    }
    return s;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    long arr[9];
    int m;
    char c;

    for (int i = 0; i < 9; i++) {
        arr[i] = 0;
    }

    while (cin >> m >> c) {
        arr[m]++;
    }
    cin >> m;
    arr[m]++;

    for (int i = 0; i < 256; i++) {
            long newArr[9];
            for (int i = 0; i < 9; i++) {
                newArr[i] = 0;
            }
            for (int j = 0; j < 9; j++) {
                if (j == 0) {
                    newArr[6] += arr[0];
                    newArr[8] += arr[0];
                } else {
                    newArr[j - 1] += arr[j];
                }
            }
            for (int j = 0; j < 9; j++) {
                arr[j] = newArr[j];
            }
            if (i == 79) {
                cout << "Part 1: " << sum(arr) << "\n";
            }
        }
    cout << "Part 2: " << sum(arr) << "\n";

    return 0;
}