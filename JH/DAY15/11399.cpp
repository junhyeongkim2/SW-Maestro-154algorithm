#include <bits/stdc++.h>
using namespace std;



vector<int>v;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    for (int i = 0; i <n ; ++i) {
        int a;
        cin >> a;
        v.push_back(a);
    }

    std::sort(v.begin(), v.end());

    int sum =0;
    int ans =0;

    for (int i = 0; i <n ; ++i) {
        ans += v[i];
        sum += ans;
    }
    cout << sum << "\n";



}