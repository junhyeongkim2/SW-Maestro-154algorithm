#include <bits/stdc++.h>

using namespace std;

int n;
int grape[10001];
int dp[10001];

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    for (int i = 1; i <=n ; ++i) {
        cin >> grape[i];
    }
    dp[0] = 0;
    dp[1] = grape[1];
    dp[2] = grape[1]+grape[2];

    int ans = dp[2];

    for (int i = 3; i <=n ; ++i) {
        dp[i] = max( dp[i-1] , max(dp[i-3]+grape[i-1]+ grape[i] ,dp[i-2] + grape[i]));
        //cout << dp[i] <<"\n";
        ans = max (dp[i],ans);
    }
    cout << ans << "\n";


}






