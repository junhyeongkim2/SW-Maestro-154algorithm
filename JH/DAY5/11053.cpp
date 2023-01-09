#include <bits/stdc++.h>

using namespace std;

int n;
int arr[1001];
int dp[1001];

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    for (int i = 0; i <n ; ++i) {
        cin >> arr[i];
        dp[i] =1;
    }

    int ans = 1;
    for (int i = 0; i <n ; ++i) {
        for (int j = 0; j <i ; ++j) {
            if(arr[i] > arr[j]) {
                dp[i] = max(dp[i],dp[j]+1);
                ans = max(ans,dp[i]);
                //cout << dp[i] << "\n";
            }
        }
        //cout << "\n";
    }

    cout << ans << "\n";






}






