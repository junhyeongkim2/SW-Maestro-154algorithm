#include <bits/stdc++.h>

using namespace std;

int n;
long long arr[1001];
long long dp[1001];

int main(){

    cin >> n;

    for (int i = 0; i <n; ++i) {
        cin >> arr[i];
        dp[i] = 1;
    }

    long long ans = 1;

    for (int i = 0; i <n; ++i) {
        for (int j = 0; j <i ; ++j) {
            if(arr[i]<arr[j]){
                dp[i]= max(dp[i],dp[j]+1);
            }
            if(ans<dp[i]){
                ans = dp[i];
            }
        }
    }
    cout << ans <<"\n";
}






