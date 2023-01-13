#include <bits/stdc++.h>
using namespace std;

int n;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string s;

    while(getline(cin,s)){
        int a=0,b=0,c=0,d=0;

        for (int i = 0; i <s.length() ; ++i) {
            if((s[i]+0) == 32){
                d++;
            }
            if((s[i]+0) >= 65 && (s[i]+0) <=90 ){
                a++;
            }
            if( (s[i]+0) >= 97 && s[i]+0 <=122){
                b++;
            }
            if( (s[i]+0) >= 48 && s[i]+0 <=57 ){
                c++;
            }

        }

        cout << b << " " << a << " " << c << " " << d << "\n";

    }



}
