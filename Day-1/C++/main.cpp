#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    vector<int> v;
    int m, ans1 = 0, ans2 = 0;

    while (cin >> m) {
        v.push_back(m);
    }

    // Part 1
    for (int i = 1; i < v.size(); i++) {
        if (v[i] > v[i - 1]) {
            ans1++;
        }
    }
    cout << "Part 1: " << ans1 << "\n";

    // Part 2
    for (int i = 3; i < v.size(); i++) {
        if (v[i] > v[i - 3]) {
            ans2++;
        }
    }
    cout << "Part 2: " << ans2 << "\n";

    return 0;
}