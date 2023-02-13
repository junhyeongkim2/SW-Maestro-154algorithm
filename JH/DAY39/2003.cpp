#import <bits/stdc++.h>
using namespace std;


int N;
long long int M;

vector<long long int>v;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    for(int i = 0 ; i < N; i++){
        long long int a;
        cin >> a;
        v.push_back(a);
    }


    int ans =0;

    for(int i = 0 ; i< N; i++){
        long long int sum =0;
        for(int j=i;j<N;j++){
            sum +=  v[j];
            if(sum == M){
                ans++;
            }
        }
    }

    cout << ans << "\n";

}