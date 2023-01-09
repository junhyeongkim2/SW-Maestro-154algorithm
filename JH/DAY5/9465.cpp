#include <bits/stdc++.h>

using namespace std;


int t;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> t;

    while(t--){
        int n ;
        int dp[2][100001];
        cin >> n;

        dp[0][0] = 0;
        dp[1][0] = 0;

        for (int i = 1; i <=n ; ++i) {
            cin >> dp[0][i];
        }
        for (int i = 1; i <=n ; ++i) {
            cin >> dp[1][i];
        }

        for (int i = 2; i <=n ; ++i) {
            dp[0][i] = max(dp[1][i-1],dp[1][i-2] ) + dp[0][i];
            dp[1][i] = max(dp[0][i-1],dp[0][i-2] ) + dp[1][i];;

        }
        cout << max(dp[1][n],dp[0][n]) << "\n";
    }


}





