#include <bits/stdc++.h>
using namespace std;


int n;
vector<pair<pair<int,string>,int >>v1;


bool comp(pair<pair<int,string>,int>a,pair<pair<int,string>,int>b  ){
    if(a.first.first==b.first.first){
        return a.second < b.second;
    }else{
        return a.first.first < b.first.first;
    }
}

int main(){

    cin >> n;

    for (int i = 0; i <n ; ++i) {
        int a;
        string b;
        cin >> a >> b;
        v1.push_back({{a,b},i});
    }
    std::sort(v1.begin(), v1.end(),comp);

    for (int i = 0; i <n ; ++i) {
        cout << v1[i].first.first << " " << v1[i].first.second << "\n";

    }


}






