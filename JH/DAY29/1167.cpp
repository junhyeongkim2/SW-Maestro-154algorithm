#import <bits/stdc++.h>

using namespace std;



int n;
vector<pair<int,int>>v[100001];
int visited[100001];


vector<pair<int,int>>m;

void dfs(int x,int dis){

    visited[x]=1;

    for(int i = 0 ; i < v[x].size();i++){
        int nx = v[x][i].first;
        int nd = v[x][i].second;
        if(visited[nx]==0){
            m.push_back({(dis+nd),nx});
            dfs(nx,dis+nd);
        }
    }


}


int main(){

    cin >> n;


    for(int i = 1 ; i <= n ; i++){
        int x;
        cin >> x;
        while(true){
            int a =0;
            cin >> a;

            if(a ==-1){
                break;
            }else{
                int b =0;
                cin >> b;
                v[x].push_back({a,b});
                v[a].push_back({x,b});
            }
        }
    }
    dfs(1,0);


    std::sort(m.begin(),m.end(),greater<>());
    int node = m[0].second;
    memset(visited,0,sizeof visited);
    m.clear();
    dfs(node,0);

    std::sort(m.begin(),m.end(),greater<>());
    cout << m[0].first;
















}