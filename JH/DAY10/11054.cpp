#include <bits/stdc++.h>
using namespace std;


int n;
int arr[1001];
int arr2[1001];
int dp[1001];
int dp2[1001];

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n ;

    for (int i = 0; i <n ; ++i) {
        int a;
        cin >> a;
        arr[i] = a;
        dp[i]=1;
        dp2[i]=1;
    }

    int ans=0;

    for (int i = 0; i <n ; ++i) {
        for (int j = 0; j <i ; ++j) {
            if(arr[i]>arr[j]&&dp[i]<dp[j]+1){
                dp[i] = dp[j]+1;
            }
        }
    }

    for (int i = n-1; i >=0 ; --i) {
        for (int j = n-1; j >i; --j) {
            if(arr[i]>arr[j]&& dp2[i]<dp2[j]+1){
                dp2[i] = dp2[j]+1;
            }
        }
    }
    for (int i = 0; i <n ; ++i) {
        ans = max ( ans, dp[i] + dp2[i] -1 ) ;
    }

    cout << ans <<"\n";





}
