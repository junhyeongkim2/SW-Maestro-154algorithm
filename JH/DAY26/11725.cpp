#import <bits/stdc++.h>

using namespace std;

int n ;
int arr[100001];
vector<int>v[100001];
int visited[100001];

void dfs(int x){

    visited[x]=1;

    for(int i = 0 ; i < v[x].size(); i ++){
        int nx = v[x][i];
        if(visited[nx]==0){
            arr[nx]=x;
            visited[nx]=1;
            dfs(nx);

        }
    }
}

int main(){

    cin >> n;

    for(int i = 0; i < n-1; i++){
        int a=0;
        int b=0;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);

    }
    dfs(1);

    for(int i = 2 ; i <=n;i++){
        cout << arr[i] << "\n";
    }





}