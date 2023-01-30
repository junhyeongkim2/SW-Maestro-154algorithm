#include <bits/stdc++.h>
#define ll long long int
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    //72 36 18 9 3 3

    //6 3 1

    //9991 97 103

    //50 25 5 1

    while(true){
        for (int i = 2; i <=n ; ++i) {
            if(n%i==0){
                n = n/i;
                //cout << n << " " << i << "\n";
                cout << i << "\n";
                break;
            }
        }
        if(n==1){
            break;
        }
    }
}