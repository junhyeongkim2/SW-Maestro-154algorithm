#import <bits/stdc++.h>
using namespace std;


int T;
bool prime[10000];
int check[10000];


void findPrime(){
    for(int i = 2 ; i*i < 10000; i++){
        if(prime[i]==false) continue;
            for(int j = i*i ; j <10000; j+=i ){
                prime[j]=false;
            }
    }
}
void bfs(int start, int dest){

    queue<int>q;
    q.push({start});
    check[start] = 0;

    while(!q.empty()){
        int x = q.front();
        q.pop();
        if(x == dest) return;

        for(int i = 0 ; i < 4; i++){
            int sep[4] = {(x/1000),(x/100)%10, (x%100)/10,x%10};
            for(int j=0; j<=9; j++ ){
                if(sep[i]==j)continue;
                sep[i]=j;
                int realNum = sep[0] * 1000 + sep[1] * 100 + sep[2] * 10 + sep[3];
                if(realNum>1000 && prime[realNum] == true && check[realNum] == -1 ){
                    check[realNum] = check[x] + 1;
                    q.push(realNum);
                }
            }
        }
    }




}


int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    memset(prime,true,sizeof prime);
    findPrime();
    cin >> T;
    int start,dest;

    while(T--){
        memset(check,-1,sizeof check);
        cin >> start >> dest;
        bfs(start,dest);
        if(check[dest]==-1) cout << "Impossible" << "\n";
        else cout << check[dest] << "\n";

    }





}