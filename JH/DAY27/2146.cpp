#import <bits/stdc++.h>

using namespace std;

int n;
int graph[100][100]={0,};
int visited[100][100];

typedef struct

{

    int y, x;

}Dir;


Dir moveDir[4] = {{1, 0}, {-1, 0}, {0, 1},{0, -1}};


int dx[4] = {1,0,0,-1};
int dy[4] = {0,1,-1,0};

void dfs(int y, int x,int cnt){

    visited[y][x] = 1;
    graph[y][x]=cnt;

    for(int i = 0 ; i < 4; i++){
        int ny = y + dy[i];
        int nx = x + dx[i];
        if(!visited[ny][nx] && graph[ny][nx] && ny>=0&&nx>=0&&ny<n&&nx<n){
            dfs(ny,nx,cnt);
        }
    }
}

int bfs(int cnt){
    queue<pair<int,int>> q;

    for(int i = 0 ; i < n; i++){
        for(int i1=0; i1 <n; i1++){
            if(graph[i][i1]==cnt){
                q.push({i,i1});
            }
        }
    }
    int res=0;

    while(!q.empty()){
        int size = q.size();

        for(int i = 0 ; i < size;i++){
            int y = q.front().first;
            int x = q.front().second;
            q.pop();

            for(int j=0;j<4;j++){
                int ny = y + dy[j];
                int nx = x + dx[j];
                if(nx>=0 && ny>=0&&nx<n&&ny<n){
                    if(graph[ny][nx]&&graph[ny][nx]!=cnt){
                        return res;
                    }else if (visited[ny][nx]==0 && !graph[ny][nx]) {
                        visited[ny][nx]=1;
                        q.push({ny,nx});
                    }
                }

            }

        }
        res++;
    }
}


int main(){

    cin >> n;

    for(int i = 0 ; i < n; i++){
        for(int i1=0; i1<n; i1++){
            cin >> graph[i][i1];
        }
    }

    int cnt = 1;

    for(int i = 0 ; i < n; i++){
        for(int i1=0; i1 < n; i1++){
            if(graph[i][i1] && visited[i][i1]==0){
                dfs(i,i1,cnt++);
            }

        }
    }


    int result = 987654321;

    for(int i=1;i<cnt;i++){
        memset(visited,0,sizeof visited);
        result = min( result,bfs(i));
    }
    cout << result << "\n";

}