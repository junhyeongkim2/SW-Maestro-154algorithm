#include <bits/stdc++.h>

using namespace std;

int n,m;
vector<int>v1;

int main(){

    cin >> n >> m;
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    for (int i = 0; i <n+m ; ++i) {
        int a;
        cin >> a;
        v1.push_back(a);
    }
    std::sort(v1.begin(), v1.end());
    for (int i = 0; i <v1.size() ; ++i) {
        cout << v1[i]<<" ";
    }

}