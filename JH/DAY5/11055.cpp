#include <bits/stdc++.h>

using namespace std;

int n;
long long arr[1001];
long long  dp[1001];
long long  ans =0;

int main(){
    cin >> n;
    for (int i = 0; i <n ; ++i) {
        cin >> arr[i];
        dp[i] = arr[i];

    }
    for (int i = 0; i <n ; ++i) {
        for (int j = 0; j <i ; ++j) {
            if(arr[i]>arr[j] && dp[i] < arr[i] + dp[j] ){
                dp[i] = dp[j] + arr[i];
            }
        }
        if(ans < dp[i])
            ans = dp[i];
    }
    cout << ans <<"\n";
}






