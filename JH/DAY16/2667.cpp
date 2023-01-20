#include <bits/stdc++.h>
using namespace std;

int n;
int graph[26][26];
int visited[26][26];

int dx[4] = {0,1,0,-1};
int dy[4] = {1,0,-1,0};



int bfs(int x, int y){
    queue<pair<int,int>>q;
    q.push({x,y});
    int b=0;
    visited[x][y]=1;
    while(!q.empty()){
        int cx = q.front().first;
        int cy = q.front().second;
        b++;
        q.pop();
        for (int i = 0; i < 4 ; ++i) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];
            if(nx>=0&&ny>=0&&nx<n&&ny<n&&visited[nx][ny]==0&&graph[nx][ny]==1){
                q.push({nx,ny});
                visited[nx][ny]=1;
            }
        }
    }
    return b;
}



int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for (int i = 0; i <n ; ++i) {
        string s;
        cin >> s;
        for (int j = 0; j <n ; ++j) {
            graph[i][j] = s[j]-'0';
        }
    }


    vector<int>v;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <n; ++j) {
            if(visited[i][j]==0&&graph[i][j]==1){
                v.push_back(bfs(i,j));
            }
        }
    }

    cout << v.size()<<"\n";
    std::sort(v.begin(), v.end());
    for (int i = 0; i <v.size() ; ++i) {
        cout << v[i] <<"\n";
    }

}