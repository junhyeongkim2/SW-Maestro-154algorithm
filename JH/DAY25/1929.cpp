#include <bits/stdc++.h>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    int m,n;
    bool check[1000001]={false,};
    cin >> m >> n;

    for (int i = 2; i <1000001 ; ++i) {
        for (int j = i+i; j <1000001; j+=i) {
            check[j]=true;
        }
    }
    check[1]=true;

    for (int i = m; i <=n ; ++i) {
            if(check[i]==false){
             cout << i << "\n";
            }
    }



}