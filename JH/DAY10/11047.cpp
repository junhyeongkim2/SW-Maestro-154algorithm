#include <bits/stdc++.h>
using namespace std;


int n,k;

vector<int>coin;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> k;

    for (int i = 0; i <n ; ++i) {
        int a;
        cin >> a;
        coin.push_back(a);
    }

    int point = coin.size()-1;
    int ans =0;

    while(true){
        //cout << k << " " << coin[point] << "\n";
        if(k  >= coin[point]){
            ans += k / coin[point];
            k = k%coin[point];
        }
        
        point--;

        if(k==0){
            break;
        }
    }

    cout << ans;
}
