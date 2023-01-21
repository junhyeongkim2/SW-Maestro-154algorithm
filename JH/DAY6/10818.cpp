#include <bits/stdc++.h>
using namespace std;


int n;
vector<int>v1;
vector<int>v2;
int main(){
    cin >> n;
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    for (int a,i = 0; i <n ; ++i) {
        cin >> a;
        v1.push_back(a);
        v2.push_back(a);
    }
    std::sort(v1.begin(), v1.end());
    std::sort(v2.begin(), v2.end(),greater<int>());

    cout << v1[0]<< " "<< v2[0];






}






