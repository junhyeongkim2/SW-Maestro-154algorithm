#include <bits/stdc++.h>

using namespace std;


vector<int>graph[100001];
int visited[100001];

void dfs(int x){
    visited[x] = 1 ;
    for (int i = 0; i <graph[x].size() ; ++i) {
        int nx = graph[x][i];
        if(visited[nx]==0){
            dfs(nx);
        }
    }
}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    int m;

    cin >> n >> m;

    for (int i = 0; i <m ; ++i) {
        int a, b;
        cin >> a>> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    int ans = 0;
    for (int i = 1; i <=n ; ++i) {
        if(visited[i]==0){
            dfs(i);
            ans ++;
        }
    }

    cout << ans <<"\n";

}