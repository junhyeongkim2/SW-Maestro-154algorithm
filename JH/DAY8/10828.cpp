#include <bits/stdc++.h>
using namespace std;

int n;

vector<int>v1;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    int n ;
    cin >> n;

    for (int i = 0; i <n ; ++i) {
        string s;
        cin >> s;
        if(s=="push"){
            int a;
            cin >> a;
            v1.push_back(a);
        }
        if(s=="pop"){
            if(v1.size()==0){
                cout << "-1" << "\n";
            }else{
                int temp;
                temp = v1.back();
                v1.pop_back();
                cout << temp << "\n";
            }
        }
        if(s=="size"){
            cout << v1.size() << "\n";
        }
        if(s=="empty"){
            if(v1.size()==0){
                cout << "1" << "\n";
            }else{
                cout << "0" << "\n";
            }
        }
        if(s=="top"){
            if(v1.size()==0){
                cout << "-1" << "\n";
            }else{
                cout << v1.back() << "\n";
            }
        }
    }

}
