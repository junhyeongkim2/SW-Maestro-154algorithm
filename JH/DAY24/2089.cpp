#include <bits/stdc++.h>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    
    if(n==0){
        cout << 0;
        return 0;
    }
    string s;
    while(n!=0){
        if(n%2==0){
            s+='0';
            n/=-2;
        }else{
            s+='1';
            n = (n-1) / -2;
        }
    }

    std::reverse(s.begin(),s.end());
    cout << s <<"\n";

}