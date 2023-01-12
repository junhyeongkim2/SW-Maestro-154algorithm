#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long int> v1;
map<long long int,long long int>m1;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for (int i = 0; i < n; ++i) {
        long long int a;
        cin >> a;
        v1.push_back(a);
    }

    std::sort(v1.begin(), v1.end(),greater<long long int>());


    long long int max1=0;
    long long int ans =0;
    
    for (int i = 0; i <v1.size(); ++i) {
        m1[v1[i]]++;
        //cout << v1[i] << " " << m1[v1[i]] << "\n";

        if(m1[v1[i]] >= max1 ){
            max1 = m1[v1[i]];
            ans = v1[i];
        }

    }
    cout << ans <<"\n";




}
