#import <bits/stdc++.h>
using namespace std;


int n,m,k;
char graph[101][101];
string dest ;

int dx[4] = {1,0,-1,0};
int dy[4] = {0,-1,0,1};
int ans = 0 ;
int dp[100][100][100];




int dfs(int x, int y, int idx){

    if(dp[x][y][idx] != -1){
        return dp[x][y][idx];
    }
    if(idx >= dest.size()){
        return 1;
    }

    dp[x][y][idx] = 0;

    for(int i = 0  ; i < 4 ; i ++){
        for(int j = 1 ; j <= k; j++){
            int nx = (dx[i] * j) + x;
            int ny = (dy[i] * j) + y;
            if(nx >=0 && ny>=0 && nx < n && ny < m && graph[nx][ny] == dest[idx]){
                dp[x][y][idx] += dfs(nx,ny,idx+1);
            }
        }
    }


    return dp[x][y][idx];
}


int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m >> k;


    for(int i = 0 ; i < n; i++){
        string s;
        cin >> s;
        for(int j = 0 ; j < m; j++){
            graph[i][j] = s[j];
        }
    }

    memset(dp,-1,sizeof dp);

    cin >> dest;

    for(int i = 0 ; i < n; i++){
        for(int j = 0 ; j < m; j++){
            if(graph[i][j] == dest[0]){
                ans += dfs(i,j,1);
            }
        }
    }

    cout << ans << "\n";


}