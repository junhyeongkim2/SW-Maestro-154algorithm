#include <bits/stdc++.h>
#define MOD 1000000
using namespace std;
long long int dp[5001];

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string s;
    cin >> s;
    int size = s.size();
    dp[0]=1;
    dp[1]=1;
    if(s[0]=='0'){
        cout << "0"<<"\n";
    }else{
        for (int i = 2; i <=size ; ++i) {
            if(s[i-1]-'0'>0) dp[i] = dp[i-1] % MOD;
            int tmp = (s[i-2]-'0') * 10 + (s[i-1]-'0');
            if(tmp>=10&&tmp<=26){
                dp[i]=(dp[i]+dp[i-2])%MOD;
            }
        }

        cout << dp[size];
    }






}