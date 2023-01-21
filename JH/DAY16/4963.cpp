#include <bits/stdc++.h>
using namespace std;


int graph[51][51];
int visited[51][51];
int w,h;

int dx[8] = {0,1,0,-1,1,-1,1,-1};
int dy[8] = {1,0,-1,0,1,1,-1,-1};

void dfs(int y, int x){

    visited[y][x]=1;
    //cout << x << " " << y << "\n";

    for (int i = 0; i <8; ++i) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(visited[ny][nx]==0&&graph[ny][nx]==1&&nx>=0&&ny>=0&&nx<w&&ny<h){
            dfs(ny,nx);
        }
    }
}



int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    while(true){
        cin >> w >> h;

        if(w==0&&h==0){
            break;
        }

        for (int i = 0; i < h; ++i) {
            for (int j = 0; j <w; ++j) {
                cin >> graph[i][j];
            }
        }

        int cnt=0;
        for (int i = 0; i <h ; ++i) {
            for (int j = 0; j <w; ++j) {
                if(visited[i][j]==0&&graph[i][j]==1){
                    dfs(i,j);
                    cnt++;
                }
            }
        }


        cout << cnt <<"\n";
        memset(visited,0,sizeof visited);
        memset(graph,0,sizeof graph);

    }

}