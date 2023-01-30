#import <bits/stdc++.h>

using namespace std;

int M,N;
int visited[1001][1001];
int graph[1001][1001];

queue<pair<pair<int,int>,int>> q;


int dx[4] = {1,0,0,-1};
int dy[4] = {0,-1,1,0};

int bfs(){

    int sum=0;
    while(!q.empty()){
        int y  = q.front().first.first;
        int x  = q.front().first.second;
        sum = q.front().second;
        q.pop();
        visited[y][x]=1;
        for(int i = 0 ; i < 4;i++){
            int ny = y+dy[i];
            int nx = x+dx[i];
            if(visited[ny][nx]==0 && nx>=0&&ny>=0&&nx<M&&ny<N&&graph[ny][nx]==0){
                q.push({{ny,nx},sum+1});
                graph[ny][nx]=1;
                visited[ny][nx]=1;
//                for(int i = 0 ; i < N; i++){
//                    for(int j = 0 ; j < M ; j++){
//                        //cout <<  graph[i][j] << " ";
//                    }
//                    //cout << "\n";
//                }
//                //cout << "\n";
//                //cout << "---------------------"<<"\n";
            }
        }
    }
    return sum;
}


int main(void){

    cin >> M  >> N;

    for(int i = 0 ; i < N; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> graph[i][j];
        }
    }

    for(int i = 0 ; i < N; i++){
        for(int j = 0 ; j < M ; j++){
            if(graph[i][j]==1){
                q.push({{i,j},0});
            }
        }
    }


    int ans = bfs();

    bool check = false;
    for(int i = 0 ; i < N; i++){
        for(int j = 0 ; j < M ; j++){
            if(graph[i][j]==0){
                check = true;
            }
        }
    }

    if(check==true){
        cout << -1;
    }else{
        cout << ans;
    }








}