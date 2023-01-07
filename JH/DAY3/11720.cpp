#include <bits/stdc++.h>

using namespace std;


int a;
string s;

int main(){

    cin >> a;
    cin >> s;

    int sum = 0;

    for (int i = 0; i <s.length() ; ++i) {
        sum += (s[i] - '0');
    }

    cout << sum << "\n";

}
