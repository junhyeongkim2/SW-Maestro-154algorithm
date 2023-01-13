#include <bits/stdc++.h>
using namespace std;

int n;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    string s;
    cin >> s;

    vector<string>v1;


    for (int i = 0; i <s.length() ; ++i) {

        v1.push_back(s.substr(i,s.length()));

    }
    std::sort(v1.begin(), v1.end());
    for (int i = 0; i <v1.size() ; ++i) {
        cout << v1[i] << "\n";
    }









}
