#include <bits/stdc++.h>
#define RED 1
#define BLUE 2
using namespace std;

int k;
int v,e;


int visited[20001];
vector<int>graph[20001];

void dfs(int x){

    if(visited[x]==0) visited[x]= 1;
    for (int i = 0; i <graph[x].size() ; ++i) {
        int next = graph[x][i];
        if(!visited[next]){
            if(visited[x]==RED){
                visited[next]=BLUE;
            }else{
                visited[next]=RED;
            }
            dfs(next);
        }
    }
}

int check(){
    for (int i = 1; i <= v; ++i) {
        for (int j = 0; j <graph[i].size() ; ++j) {
            int next = graph[i][j];
            if(visited[i] == visited[next]){
                return 0;
            }
        }
    }
    return 1;
}


int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> k;

    while(k--){
        cin >> v >> e;

        for (int i = 0; i <e ; ++i) {
            int a,b;
            cin >> a >> b;
            graph[a].push_back(b);
            graph[b].push_back(a);
        }
        for (int i = 1; i <=v ; ++i) {
            if(visited[i]==0){
                dfs(i);
            }
        }


        if(check()){
            cout << "YES"<< "\n";
        }else{
            cout << "NO" << "\n";
        }

        memset(visited,0,sizeof visited);
        for (int i = 0; i <=v ; ++i) {
            graph[i].clear();
        }
    }
    
}