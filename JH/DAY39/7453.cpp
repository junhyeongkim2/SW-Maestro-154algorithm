#import <bits/stdc++.h>
using namespace std;

//누적합, 투포인터 문제, 왼쪽 오른쪽을 한꺼번에 누적합을 구하면 시간초과가 나기 때문에 
//왼쪽과 오른쪽을 나누어서 누적합을 구하고 이분탐색 lower_bound, upper_bound를 통해서 0인 값을 찾아줌

int n;
int arr[4001][4];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < 4; j++){
            cin >> arr[i][j];
        }
    }

    vector<int>a;
    vector<int>b;


    for(int i = 0; i < n; i++){
        for(int j = 0 ; j < n; j++){
            a.push_back(arr[i][0]+arr[j][1]);
            b.push_back(arr[i][2]+arr[j][3]);
        }
    }

    sort(a.begin(),a.end());
    sort(b.begin(),b.end());

    long long int ans = 0 ;

    for(int i = 0 ; i < a.size();i++){
        int B_pre = lower_bound(b.begin(),b.end(),-a[i]) - b.begin();
        int B_end = upper_bound(b.begin(),b.end(),-a[i]) - b.begin();
        ans += (B_end - B_pre) ;
    }

    cout << ans << "\n";




}