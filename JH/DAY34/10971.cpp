#import <bits/stdc++.h>
using namespace std;


int n;
int m[11][11];
int visit_check[11];
int mcost = 2e9;
int start_city;


void search(int visit_city, int cnt, int cost){
    visit_check[visit_city]= true;
    if(cnt == n){
        if(m[visit_city][start_city] > 0){
            mcost = min(cost+m[visit_city][start_city],mcost);
        }
        return;
    }


    for(int i = 0; i < n; i++){
        if(m[visit_city][i] == 0 ) continue;
        if(visit_check[i]==true) continue;
        search(i,cnt+1,cost+m[visit_city][i]);
        visit_check[i] = false;
    }

    visit_check[visit_city]=false;

}


int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    for(int i = 0 ; i < n; i++ ){
        for(int j = 0; j < n ; j++){
            cin >> m[i][j];
        }
    }

    for(int i = 0  ; i < n ; i ++){
        start_city = i;
        search(i,1,0);
    }

    cout << mcost;

}