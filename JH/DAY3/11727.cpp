#include <bits/stdc++.h>

using namespace std;


int a;
int dp[1001];

int main(){

    cin >> a;

    dp[1] = 1;
    dp[2] = 3;

    for (int i = 3; i <1001 ; ++i) {
        dp[i] = ((dp[i-2] * 2) + dp[i-1]) % 10007;
    }

    cout << dp[a];

}





