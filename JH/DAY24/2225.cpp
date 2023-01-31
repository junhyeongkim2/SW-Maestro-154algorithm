#include <bits/stdc++.h>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, k ;
    int dp[201][201];
    cin >> n >> k;

    for (int i = 1; i <= k; ++i) {
        dp[1][i] =i;
    }

    for (int i = 2; i <= n; ++i) {
        for (int j = 1; j <=k ; ++j) {
            dp[i][j] = (dp[i][j-1] + dp[i-1][j])%1000000000 ;
        }
    }
    cout << dp[n][k];

}