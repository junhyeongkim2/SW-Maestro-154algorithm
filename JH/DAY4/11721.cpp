#include <bits/stdc++.h>

using namespace std;

string s;

int main(){

    cin >> s;

    int cnt =0;

    for (int i = 0; i <s.length() ; ++i) {
        cout << s[i];
        cnt ++ ;
        if(cnt>=10){
            cnt=0;
            cout << "\n";
        }
    }

}





