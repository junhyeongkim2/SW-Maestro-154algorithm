#include <bits/stdc++.h>
using namespace std;


int n;
vector<int>v1;

int main(){
    cin >> n;

    for (int a,i = 0; i <n ; ++i) {
        cin >> a;
        v1.push_back(a);
    }
    std::sort(v1.begin(), v1.end());
    for (int i = 0; i <n ; ++i) {
        cout << v1[i]<<"\n";

    }




}






