#include <bits/stdc++.h>
using namespace std;


bool comp(pair<int,int>a,pair<int,int>b){

    if(a.second == b.second){
        return a.first < b.first;
    }
    return a.second < b.second;
}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;

    cin >> n;

    vector<pair<int,int>>v;

    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        v.push_back({a,b});
    }

    std::sort(v.begin(), v.end(),comp);

    for (int i = 0; i <n ; ++i) {
        //cout << v[i].first << " " <<v[i].second << "\n";
    }

    //cout << "---------"<<"\n";

    int end = v[0].second;
    int ans =1;
    for (int i = 1; i <n ; ++i) {
        if(end <= v[i].first){
            //cout << end << " " << v[i].first <<"\n";
            end = v[i].second;
            ans ++;
        }
    }
    cout << ans <<"\n";


}