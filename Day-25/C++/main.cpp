#include <bits/stdc++.h>
#include <utility>
#include <map>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    map<pair<int, int>, int> m;
    string line, pt = ".>v";
    int row = 0, col = 0;

    while (cin >> line) {
        if (col == 0) {
            col = line.length();
        }
        for (int c = 0; c < col; c++) {
            if (line[c] != pt[0]) {
                pair<int, int> p (row, c);
                m[p] = line[c] == pt[1] ? 1 : 2;
            }
        }
        row++;
    }

    bool noChange = false;
    int ctr = 0;

    while (!noChange) {
        noChange = true;
        map<pair<int, int>, int> m1, m2;
        
        for (const auto &p : m) {
            if (p.second == 1) {
                pair<int, int> p2 (p.first.first, (p.first.second + 1) % col);
                if (m.find(p2) == m.end()) {
                    noChange = false;
                    m1[p2] = 1;
                } else {
                    m1[p.first] = 1;
                }
            } else {
                m1[p.first] = 2;
            }
        }

        for (const auto &p : m1) {
            if (p.second == 2) {
                pair<int, int> p2 ((p.first.first + 1) % row, p.first.second);
                if (m1.find(p2) == m1.end()) {
                    noChange = false;
                    m2[p2] = 2;
                } else {
                    m2[p.first] = 2;
                }
            } else {
                m2[p.first] = 1;
            }
        }
        
        m = m2;
        ctr++;
    }

    cout << "Part 1: " << ctr << endl;
    cout << "Part 2: THE END!" << endl;

    return 0;
}