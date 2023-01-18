#include <bits/stdc++.h>
using namespace std;

int n;


int arr[100];

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string s;
    cin >> s;


    for (int i = 0; i <s.size() ; ++i) {
        arr [ s[i] - 97  ] ++ ;
    }


    for (int i = 0; i <26 ; ++i) {
        cout << arr[i] << " ";
    }

}
