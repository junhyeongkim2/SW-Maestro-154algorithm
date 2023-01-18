#include <bits/stdc++.h>
using namespace std;

int n;


int arr[100] = {-1,};

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string s;
    cin >> s;

    for (int i = 0; i <101 ; ++i) {
        arr[i]=-1;
    }

    for (int i = s.size()-1; i >=0 ; --i) {
        //cout << s[i] << " "<< s[i]-97 <<"\n";
        arr [ s[i] - 97  ] = i;
    }

    for (int i = 0; i <26 ; ++i) {
        cout << arr[i] << " ";
    }

    //1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

}
