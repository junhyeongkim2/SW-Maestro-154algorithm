#include <bits/stdc++.h>
using namespace std;

int n;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    int a, b;
    cin >> a >> b;

    vector<int>v1;

    for (int i = 0; i < a; ++i) {
        int a;
        cin >> a;
        v1.push_back(a);
    }
    std::sort(v1.begin(), v1.end());

    cout << v1[b-1];

}
