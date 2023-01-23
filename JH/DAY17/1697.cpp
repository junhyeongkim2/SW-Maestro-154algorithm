#include <bits/stdc++.h>
using namespace std;

int n,k;
int visited[100002];

void bfs(int x){

    queue <pair<int,int>> q;
    q.push({x,0});

    while(!q.empty()){
        int cx = q.front().first;
        int cnt = q.front().second;
        q.pop();
        if(cx == k){
            cout << cnt;
            break;
        }



        for (int i = 0; i <3 ; ++i) {
            int nx = 0;
            if(i==0){
                nx = cx - 1;
            }
            if(i==1){
                nx = cx + 1;
            }
            if(i==2){
                nx = cx * 2;
            }
            if(nx>=0 && nx <=100001){
                if(visited[nx]==0){
                    visited[nx]=1;
                    q.push({nx,cnt+1});
                }

            }
        }

    }



}



int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> k;
    visited[n]=1;
    bfs(n);

    return 0;

}