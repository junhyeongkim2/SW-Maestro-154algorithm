#include <bits/stdc++.h>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    int small[101];
    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> small[i];
    }


    bool check[1001]={false,};

    check[1]=true;
    for (int i = 2; i <1001 ; ++i) {
        for (int j = i+i; j <1001; j+=i) {
            check[j]=true;
        }
    }

    int ans =0;
    for (int i = 0; i <n ; ++i) {
            if(check[small[i]]==false){
                ans++;
            }
    }
    cout << ans ;






}