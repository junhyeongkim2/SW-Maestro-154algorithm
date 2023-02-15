#import <bits/stdc++.h>
using namespace std;


//시간초과 때문에 left와 right를 나누어 S가 되는 부분 수열 탐색

int n,s;

int v[41];
long long result=0;
map<int,int>total;

void leftdfs(int x,int sum ){

    if(x == n/2){
        total[sum]++;
        return;
    }

    leftdfs(x+1,sum+v[x]);
    leftdfs(x+1,sum);

}

void rightdfs(int x,int sum){

    if(x==n){
        result += total[s-sum];
        return;
    }

    rightdfs(x+1,sum);
    rightdfs(x+1,sum+v[x]);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> s;

    for(int i = 0 ; i < n ; i++){
        int a;
        cin >> a;
        v[i]=a;
    }


    leftdfs(0,0);
    rightdfs(n/2,0);

    if(s==0){
        result--;
    }

    cout << result <<"\n";
}