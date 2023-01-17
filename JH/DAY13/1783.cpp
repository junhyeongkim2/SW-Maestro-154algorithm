#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,m;

    cin >> n >> m;

    if(n==1){
        cout << 1;
    }
    if(n==2){
        cout << min(4,(m-1)/2+1);
    }
    if(n>=3){
        if(m<7){
            cout << min(4,m);
        }else if (m>=7){
            cout << 5+m-7;
        }


    }


}