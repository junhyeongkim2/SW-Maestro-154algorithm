#import <bits/stdc++.h>

using namespace std;
int n;
int m;
map<int,int>ma;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n;
    for(int i = 0 ; i < n; i ++){
        int a;
        cin >> a;
        ma[a]++;
    }

    cin >> m;
    vector<int>v;

    for(int i = 0 ; i < m; i++) {
        int a;
        cin >> a;
        cout << ma[a] << " ";
    }

}