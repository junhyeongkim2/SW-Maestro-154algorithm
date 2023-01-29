#include <bits/stdc++.h>
using namespace std;

long long d2(long long N){
    long long cnt = 0;
    for(long long i = 2; i<=N; i*=2){
        cnt += N / i;
    }
    return cnt;
}

long long d5(long long N){
    long long cnt =0;
    for (long long i = 5; i <=N ; i*=5) {
        cnt += N / i;
    }
    return cnt;
}


int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long n,m;
    cin >> n >> m;

    cout << min(d5(n) - d5(n-m) - d5(m),d2(n)-d2(n-m)-d2(m));


}