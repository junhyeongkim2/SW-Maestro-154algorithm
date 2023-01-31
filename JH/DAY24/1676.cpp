#include <bits/stdc++.h>
#define ll long long int
using namespace std;
int n;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    
    ll ans = 0;

    for (int i = 5; i <=n ; i*=5) {
        ans += n / i ;
    }
    cout << ans << "\n";




}