#include <bits/stdc++.h>
using namespace std;



int n,m;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    vector<int>tree;

    int maxtree=0;

    for (int i = 0; i <n ; ++i) {
        int a;
        cin >> a;
        tree.push_back(a);
        maxtree = max(maxtree,a);
    }

    long long int low = 1;
    long long int high = maxtree;

    long long int ans =0;

    while(low<=high){
        long long int mid = (low+high)/2;
        long long int remainder = 0;

        for (int i = 0; i <tree.size(); ++i) {
            if(tree[i] >= mid){
                remainder += (tree[i] - mid);
            }
        }

        if(remainder >= m ){
            ans = max(ans,mid);
            low = mid+1;
        }else{
            high = mid-1;
        }


    }

    cout << ans <<"\n";

}