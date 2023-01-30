#include <bits/stdc++.h>
#define ll long long int
using namespace std;
int n;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    int ans = 1 ;
    for (int i = 1; i <=n ; ++i) {
        ans = i * ans ;
        //cout << ans <<"\n";
    }
    cout << ans <<"\n";

}