#import <bits/stdc++.h>
using namespace std;


int n;
int s;
int graph[20];
int cnt =0;

void dfs(int i, int sum){
    if(i == n){
        return;
    }
    if(sum + graph[i] == s){
        cnt++;
    }
    dfs(i+1,sum);
    dfs(i+1,sum+graph[i]);
}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> s;

    for(int i = 0 ; i < n; i ++){
        cin >> graph[i];
    }

    dfs(0,0);


    cout << cnt <<"\n";

}