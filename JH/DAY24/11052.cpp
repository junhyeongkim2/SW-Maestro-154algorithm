#include <bits/stdc++.h>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    int dp[1001]={0,};
    int card[1001];

    for (int i = 1; i <=n ; ++i) {
        cin >> card[i];
        dp[i] = card[i];
    }

    for (int i = 1; i <=n ; ++i) {
        for (int j = 1; j <=i ; ++j) {
            dp[i] = max(dp[i], dp[i-j]+dp[j] );
        }
    }

    cout << dp[n];

}