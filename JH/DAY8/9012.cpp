#include <bits/stdc++.h>
using namespace std;

int n;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;

    while(t--){
        bool check = false;
        stack<int>s;
        string a;
        cin >> a;
        for (int i = 0; i < a.length(); ++i) {
            if(a[i] == '('){
                s.push(a[i]);
            }else if(a[i] == ')'){
                if(s.size()==0){
                    check = true;
                    cout << "NO" << "\n";
                    break;
                }
                if(s.top() == '('){
                    s.pop();
                }
            }
        }

        if(check == false && s.size()==0){
            cout << "YES" << "\n";
        }else if (s.size()!=0){
            cout << "NO" << "\n";
        }
    }
}
