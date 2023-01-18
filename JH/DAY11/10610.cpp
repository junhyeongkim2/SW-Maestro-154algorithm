#include <bits/stdc++.h>
using namespace std;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string s;
    cin >> s;
    std::sort(s.begin(), s.end(),greater<>());


    if(s[s.length()-1] != '0'){
        cout << -1;
    }else{
        int sum=0;
        for (int i = 0; i <s.length()-1 ; ++i) {
            sum += s[i]-'0';
            //cout << sum <<"\n";

        }
        if(sum%3==0){
            cout << s;
        }else{
            cout << -1;
        }
    }


}
