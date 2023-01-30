#import <bits/stdc++.h>

using namespace std;

int N,M;

int graph[101][101];
int visited[101][101];

int dx[4]= {1,0,0,-1};
int dy[4]= {0,-1,1,0};

int bfs(){

    queue<pair<pair<int,int>,int>>q;
    q.push({{0,0},1});
    int sum = 0;
    bool flag = false;

    visited[0][0]=1;

    while(!q.empty()){
        int y = q.front().first.first;
        int x = q.front().first.second;
        sum = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i ++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(visited[ny][nx] == 0 && graph[ny][nx] == 1 && ny>=0&&nx>=0&&ny<N&&nx<M){

                q.push({{ny,nx},sum+1});
                visited[ny][nx]=1;
                if(ny == N-1 && nx == M-1){
                    sum+=1;
                    flag = true;
                    break;
                }




            }
        }
        if(flag)break;
    }

    return sum;

}


int main(void){

    cin >> N >> M;


    for(int i = 0 ; i < N; i ++){
        string s;
        cin >> s;
        for(int j = 0 ; j < M; j++){
            graph[i][j] = s[j]-'0';
        }
    }

    cout << bfs();



}