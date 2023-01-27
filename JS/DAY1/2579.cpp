#include <iostream>
#define MAXN 301 // 계단 갯수

using namespace std;

int n;
int arr[MAXN];
int dp[MAXN];

int main()
{
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];

        if (i == 0)
            dp[i] = arr[i];
        if (i == 1)
            dp[i] = arr[i] + dp[i - 1];
        if (i == 2)
            dp[i] = arr[i] + max(arr[i - 1], dp[i - 2]);
    }

    for (int i = 3; i < n; i++)
    {
        dp[i] = arr[i] + max(dp[i - 2], dp[i - 3] + arr[i - 1]);
    }

    cout << dp[n - 1];
}