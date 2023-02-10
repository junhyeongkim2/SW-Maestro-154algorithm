#import <bits/stdc++.h>
using namespace std;

char graph[21][21];
map<char,int> visited;

int dx[4] = {0,0,-1,1};
int dy[4] = {1,-1,0,0};

int R,C;

int ans =0;

void dfs(int y, int x, int depth){

    ans = max(ans,depth);
    //cout << graph[y][x] <<  " / " << depth << "\n";

    for(int i = 0 ; i < 4 ; i++){
        int ny = dy[i]+y;
        int nx = dx[i]+x;
        if(visited[graph[ny][nx]]==0 && ny >=1 && nx>=1 && ny<=R&&nx<=C){
            visited[graph[ny][nx]]=1;
            dfs(ny,nx,depth+1);
            visited[graph[ny][nx]]=0;
        }
    }
}


int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> R >> C;

    for(int i = 1 ; i <= R ; i++){
        string s;
        cin >> s;
        for(int j = 1 ; j<=C; j++){
            graph[i][j] =  s[j-1];
        }
    }



    visited[graph[1][1]]=1;
    dfs(1,1,0);
    cout << ans +1 <<"\n";



}