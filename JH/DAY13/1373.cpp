#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string s;
    cin >> s;

    while(s.length()%3!=0){
        s = '0' + s;
    }

//    cout << s <<"\n";

    string num;
    for (int i = 0; i <s.length() ; i+=3) {
        num += (((s[i]-'0')*4) + ((s[i+1]-'0')*2) + ((s[i+2]-'0')*1))+'0';
    }
    cout << num <<"\n";


}