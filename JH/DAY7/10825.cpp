#include <bits/stdc++.h>
using namespace std;

int n;


vector< pair<pair<string,int>,pair<int,int>>> score;

bool comp(pair<pair<string,int>,pair<int,int>> a,pair<pair<string,int>,pair<int,int>> b ){
    if(a.first.second!= b.first.second){
        return a.first.second > b.first.second;
    }else if ( a.first.second == b.first.second&& a.second.first == b.second.first&&a.second.second == b.second.second){
        return a.first.first < b.first.first;
    }else if( a.first.second == b.first.second&& a.second.first == b.second.first){
        return a.second.second > b.second.second;
    }else if(a.first.second == b.first.second){
        return a.second.first < b.second.first;
    }

}

int main() {

    cin >> n;

    for (int i = 0; i <n ; ++i) {
        string a;
        int b,c,d;
        cin >> a>> b>> c>> d;
        score.push_back({{a,b},{c,d} });
    }

    std::sort(score.begin(), score.end(),comp);

    for (int i = 0; i <n ; ++i) {
        cout << score[i].first.first << "\n";
    }




}
