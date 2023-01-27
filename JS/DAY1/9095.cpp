#include <iostream>

using namespace std;

int t, n;
int dp[13];

int main()
{
    cin >> t;

    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;

    for (int i = 4; i < 11; i++)
    {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }
    while (t--)
    {
        cin >> n;

        cout << dp[n] << "\n";
    }
}