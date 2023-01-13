#include <bits/stdc++.h>
using namespace std;

int n;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string a;
    string b;
    string c;
    string d;

    string suma;
    string sumb;

    cin >> a >> b >> c >> d;

    suma = a+b;
    sumb = c+d;
    long long int ans = stold(suma) + stold(sumb);

    cout << ans;

}
