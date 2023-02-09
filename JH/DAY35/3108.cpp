#import <bits/stdc++.h>
using namespace std;
#define MAX 2001


int N;
int MAP[MAX][MAX];
bool visit[MAX][MAX];

int dx[] = {0,0,-1,1};
int dy[] = {1,-1,0,0};


void Input(){
    cin >> N;

    for(int i=0;i<N;i++){
        int x1,y1,x2,y2;

        cin >> x1 >> y1 >> x2 >> y2;

        x1 = (x1+500)*2;
        y1 = (y1+500)*2;
        x2 = (x2+500)*2;
        y2 = (y2+500)*2;

        for(int i = x1; i<=x2; i++){
            MAP[y1][i] = 1;
            MAP[y2][i] = 1;
        }
        for(int i = y1; i<=y2; i++){
            MAP[i][x1] = 1;
            MAP[i][x2] = 1;
        }
    }
}

void dfs(int x , int y){

    MAP[x][y] = 2;
    for(int i = 0 ; i <4;i++ ){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(MAP[nx][ny]==1&&nx>=0&&ny>=0&&nx<=2000&&ny<=2000){
            dfs(nx,ny);
        }
    }

}

void Solution(){

    int PU_cnt = 0;

    for(int i = 0 ; i <= 2000; i++){
        for(int j = 0; j <=2000; j++){
            if(MAP[i][j]==1){
                dfs(i,j);
                PU_cnt++;
            }
        }
    }

    if(MAP[1000][1000]!=0){
        PU_cnt--;
    }
    cout << PU_cnt << endl;

}


int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    Input();
    Solution();

}