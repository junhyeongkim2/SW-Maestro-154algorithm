#include <iostream>
#include <cstring> //memset

using namespace std;
const int MAX = 100000 + 1;
int N, cnt;
int want[MAX];
bool visited[MAX];
bool done[MAX]; //방문이 끝났는지 여부


void dfs(int x){

    visited[x]=true;

    int next = want[x];

    if(!visited[next]){
        dfs(next);
    }else if(!done[next]){
        for (int i = next; i !=x  ; i=want[i]) {
            cnt++;
        }
        cnt++;
    }
    done[x] = true;
}

int main(void){

    int T;
    cin >> T;

    while(T--){
        memset(visited,0,sizeof visited);
        memset(done,0,sizeof done);
        cin >> N;
        for (int i = 1; i <=N ; ++i) {
            cin >> want[i];
        }
        cnt = 0;

        for (int i = 1; i <=N ; ++i) {
            if(!visited[i])
                dfs(i);
        }

        cout << N-cnt << "\n";

    }
    return 0;



}