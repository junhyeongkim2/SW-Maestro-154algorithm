#include <bits/stdc++.h>
using namespace std;

int n;
int dp[301];
int stair[301];

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for (int i = 0; i <n ; ++i) {
        cin >> stair[i];
    }
    int ans = 0;

    dp[0] = stair[0];
    dp[1] = stair[0] + stair[1];
    dp[2] = max ( stair[0] ,stair[1]) + stair[2];


    for (int i = 3; i <n ; ++i) {
        dp[i] = max((dp[i-3] + stair[i-1]) , (dp[i-2])) + stair[i];
    }

    cout << dp[n-1] << "\n";

}
