#include <bits/stdc++.h>
#define lld long long int
using namespace std;


int k,n;
vector<lld>v;


int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> k >> n;



    lld maxv=0;
    for (int i = 0; i <k ; ++i) {
        lld a;
        cin >> a;
        v.push_back(a);
        maxv = max(maxv,a);
    }


    lld left =1;
    lld right = maxv;
    lld ans =0;

    while(left<=right){
        lld mid = (left+right)/2;
        lld sum=0;

        for (int i = 0; i <v.size() ; ++i) {
            sum+= v[i]/mid;
        }
        
        if(sum >= n){
            left = mid+1;
            ans = max(ans,mid);
        }else if(sum < n){
            right = mid-1;
        }


    }

    cout << ans <<"\n";







}