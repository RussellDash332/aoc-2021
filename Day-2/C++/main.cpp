#include <bits/stdc++.h>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    string cmd;
    long d;
    long x = 0, y1 = 0, y2 = 0;

    while (cin >> cmd >> d) {
        if (cmd.compare("forward") == 0) {
            x += d;
            y2 += y1 * d;
        } else if (cmd.compare("up") == 0) {
            y1 -= d;
        } else {
            y1 += d;
        }
    }

    cout << "Part 1: " << x * y1 << "\n";
    cout << "Part 2: " << x * y2 << "\n";

    return 0;
}