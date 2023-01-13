#include <bits/stdc++.h>
using namespace std;

int n;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string s;
    string ans;

    getline(cin,s);


    //cout << s[0]+0;
    //cout << "\n";
    //cout << s[1]+0;

    for (int i = 0; i <s.length() ; ++i) {

        if((s[i]+0) ==32){
            ans += " ";
        }
        else if(s[i]+0>=65 && s[i]+0<=90){
            if(s[i]+0<=77){
                ans += s[i]+13;
            }
            if(s[i]+0>=78){
                ans += s[i]-13;
            }

        }else if(s[i]>=97 && s[i]<=122){
            if(s[i]+0<=109){
                ans += s[i]+13;
            }
            if(s[i]+0>=110){
                ans += s[i]-13;
            }
        }else{
            ans += s[i];
        }

    }

    cout << ans << "\n";



    //A-Z 65 90
    //a-z 97 ~ 122




}
