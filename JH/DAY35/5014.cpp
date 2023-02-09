#import <bits/stdc++.h>
using namespace std;

int F,S,G,U,D;

int visited[1000001];

void bfs(int start, int dest, int cnt ){

    visited[start] = 1;

    queue <pair<int,int>>q;
    q.push({start,cnt});

    while(!q.empty()){
        int x = q.front().first;
        int qcnt = q.front().second;
        q.pop();
        if(x == G || x == G){
            //cout << Ux << " " << Dx << " " << G << " " << "\n";
            cout << qcnt << "\n";
            return;
        }
        //cout << qcnt << "\n";
        int Ux = x + U;
        int Dx = x - D;
        //cout << Ux << " " << Dx << " " << G << " " << qcnt << " " << "\n";

        if(Ux>=1&&Ux<=F&&visited[Ux]==0){
            q.push({Ux,qcnt+1});
            visited[Ux]=1;
        }
        if(Dx>=1&&Dx<=F&&visited[Dx]==0){
            q.push({Dx,qcnt+1});
            visited[Dx]=1;
        }

    }
    cout << "use the stairs" << "\n";
    return;

}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> F >> S >> G >> U >> D;

    bfs(S,G,0);


}