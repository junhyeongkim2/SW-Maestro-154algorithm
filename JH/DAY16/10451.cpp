#include <bits/stdc++.h>

using namespace std;

int graph[1001];

int getParent(int x){

    if(graph[x]==x)return x;
    return graph[x] = getParent(graph[x]);

}


void unionParent(int x, int y){

    x = getParent(x);
    y = getParent(y);

    if(x<y){
        graph[y]=x;
    }else{
        graph[x]=y;
    }
}


int findParent(int a, int b){
    a = getParent(a);
    b = getParent(b);

    if(a==b){
        return 1;
    }
        return 0;
}


int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;

    while(t--){
        int n;
        int ans =0;
        cin >> n;
        int arr[1001]={0,};

        for (int i = 1; i <= n; ++i) {
            graph[i] = i;
        }
        for (int i = 1; i <=n ; ++i) {
            int a;
            cin >> a;
            unionParent(i,a);
        }

        for (int i = 1; i <=n ; ++i) {
            int pr = getParent(i);
            //cout << pr <<"\n";
            arr[pr]++;
        }
        for (int i = 1; i <=1000 ; ++i) {
            if(arr[i]!=0){
                ans++;
            }
        }
        cout << ans << "\n";

    }



}