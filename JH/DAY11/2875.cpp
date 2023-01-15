#include <bits/stdc++.h>
using namespace std;


int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    int n,m,k;

    cin >> n >> m >> k;

    int ans =0;
    while(true){

        n-=2;
        m-=1;
        if(n+m < k || n<0 || m<0){
            cout << ans << "\n";
            break;
        }
        ans++;
    }


}
