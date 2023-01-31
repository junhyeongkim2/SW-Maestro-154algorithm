#include <bits/stdc++.h>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    bool check[1000001]={false,};

    for (int i = 2; i <1000001 ; ++i) {
        for (int j = i+i; j <1000001; j+=i) {
            check[j]=true;
        }
    }
    check[1]=true;
    vector<int>s;

    for (int i = 2; i <=1000000 ; ++i) {
            if(check[i]==false){
                s.push_back(i);
                //cout << i << "\n";
            }
    }


    while(true){
        int a;
        cin >> a;
        if(a==0){
            break;
        }
        for (int i = 0; i <s.size() ; ++i) {
            int n2 = a - s[i];

            if(check[n2]==false){
                cout << a << " = " << s[i] << " + " << n2 << "\n";
                break;
            }

        }

    }


}