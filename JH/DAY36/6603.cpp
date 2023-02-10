#import <bits/stdc++.h>
using namespace std;


int k;
vector<int>lotto;
int visited[50];


void dfs(int x, int depth, vector<int>v){

    if(depth==6){

        for(auto x : v){
            cout << x << " ";
        }
        cout << "\n";

        return;
    }

    for(int i = x+1; i<k; i++){\
        if(visited[lotto[i]]==0){
            visited[lotto[i]]=1;
            v.push_back(lotto[i]);
            dfs(i,depth+1,v);
            v.pop_back();
            visited[lotto[i]]=0;
        }
    }
}


int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    while(true){
        cin >> k;
        if ( k == 0){
            break;
        }

        for(int i = 0 ; i < k ; i++){
            int a;
            cin >> a;
            lotto.push_back(a);
        }

        for(int i=0;i<k;i++){
            vector<int>tv;
            tv.push_back(lotto[i]);
            dfs(i,1,tv);
        }

        cout << "\n";
        memset(visited,0,sizeof visited);
        lotto.clear();
    }


}