#include <bits/stdc++.h>
using namespace std;

stack<char>st;

int main(){


    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string s;
    cin >> s;

    int cnt = 0;

    for (int i = 0; i <s.length() ; ++i) {
        if(s[i] == '('){
            st.push(s[i]);
        }else{
            if(s[i-1]=='('){
                st.pop();
                cnt+=st.size();
            }else{
                if(st.size()!=0){
                    st.pop();
                    cnt++;
                }
            }
        }
    }
    cout << cnt << "\n";
}