#include <bits/stdc++.h>
using namespace std;


int n;
vector<pair<int,int>>v1;

bool comp(pair<int,int> a, pair<int,int> b){

    if(a.second==b.second){

        return a.first<b.first;

    }else{
        return a.second<b.second;
    }
}

int main(){

    cin >> n;

    for (int i = 0; i <n ; ++i) {
        int a, b;
        cin >> a >> b;
        v1.push_back({a,b});
    }
    std::sort(v1.begin(), v1.end(),comp);

    for (int i = 0; i <n ; ++i) {
        cout << v1[i].first << " " << v1[i].second << "\n";

    }


}






