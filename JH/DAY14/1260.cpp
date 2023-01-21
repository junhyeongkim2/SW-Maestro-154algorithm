#include <bits/stdc++.h>

using namespace std;


vector<int>graph[10002];
int visited[10002];

void dfs(int x){

    visited[x] = 1 ;
    cout << x << " ";

    for (int i = 0; i <graph[x].size() ; ++i) {
        int nx = graph[x][i];
        if(visited[nx]==0){
            dfs(nx);
        }
    }
}

void bfs(int x){
    queue<int>q;
    q.push(x);
    visited[x]=1;
    while(!q.empty()){
        int now = q.front();
        q.pop();
        cout << now << " ";
        for (int i = 0; i < graph[now].size() ; ++i) {
            int nx = graph[now][i];
            if(visited[nx]==0){
                visited[nx]=1;
                q.push( nx);
            }
        }
    }
}




int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    int m;
    int v;

    cin >> n >> m >> v;

    for (int i = 0; i <m ; ++i) {
        int a, b;
        cin >> a>> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i <= n;i++){
        sort(graph[i].begin(), graph[i].end()); // 낮은 숫자부터 탐색.
    }
    dfs(v);
    cout << "\n";
    memset(visited,0,10002);
    bfs(v);














}