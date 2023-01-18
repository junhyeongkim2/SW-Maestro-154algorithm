
#include <bits/stdc++.h>
using namespace std;

int main(){


    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n,m;
    vector<char>broken_button;
    cin >> n;
    cin >> m;

    for (int i = 0; i <m ; ++i) {
        char a;
        cin >> a;
        broken_button.push_back(a);
    }

    int minimum= abs(n-100);

    if(n!=100){
        for (int i = 0; i <1000001 ; ++i) {
            bool check = false;
                for (int j = 0; j <broken_button.size(); ++j) {
                    if ( to_string(i).find(broken_button[j]) == string::npos){
                    }else{
                        check=true;
                    }
                }
            if(check==false){
                int tmp = (abs(n-i)+to_string(i).length());
                minimum = min(minimum, tmp);
            }
        }
        cout << minimum <<"\n";
    }else{
        cout << "0"<<"\n";
    }

}