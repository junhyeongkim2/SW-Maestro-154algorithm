#include <bits/stdc++.h>
using namespace std;

int n;
int dp[35];

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    if(n%2==1){
        cout << "0";
        return 0;
    }
    dp[0] = 1;
    dp[1] = 0;
    dp[2] = 3;
    dp[3] = 0;

    for (int i = 4; i <= n; ++i) {
        dp[i] = dp[i-2] * dp[2];
        //cout << dp[i-2] * dp[2] << " ";
        for (int j = i-4; j >=0; j-=2) {
            dp[i] += dp[j] * 2;
            //cout << dp[j] * 2 << " ";
        }
        //cout << "\n";
    }
    cout << dp[n];
}