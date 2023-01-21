#include <bits/stdc++.h>
using namespace std;


int n;
int dp[100001];

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        dp[i] = a;
    }

    int ans = dp[0];
    for (int i = 1; i <n ; ++i) {
        dp[i] = max(dp[i-1]+dp[i],dp[i]);
        ans = max(dp[i],ans);
    }
    cout << ans << "\n";


}
