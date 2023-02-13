#import <bits/stdc++.h>
using namespace std;


// 투포인터, 누적합

long long int T;
int n;
int m;

vector<long long int>a;
vector<long long int>b;

int arr1[1001];
int arr2[1001];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> T;
    cin >> n;

    for(int i = 0 ; i < n ; i++){
        cin >> arr1[i];
    }

    cin >> m;

    for(int j = 0; j < m; j ++){
        cin >> arr2[j];
    }

    for(int i = 0 ; i < n;i++){
        long long int temp=0;
        for(int j = i; j < n; j++){
            temp+=arr1[j];
//            cout << temp << "\n";
            a.push_back(temp);
        }
    }

//    cout << "- - - - - - - - " <<"\n";
    for(int i = 0 ; i < m;i++){
        long long int temp=0;
        for(int j = i; j < m; j++){
            temp+=arr2[j];
//            cout << temp << "\n";
            b.push_back(temp);
        }
    }
//    cout << "- - - - - - - - " <<"\n";


    sort(a.begin(),a.end());
    sort(b.begin(),b.end());

    long long ans =0;
    for(int i = 0 ; i < a.size();i++){
        int b_start = lower_bound(b.begin(),b.end(), T-a[i]) - b.begin();
        int b_end = upper_bound(b.begin(),b.end(), T-a[i]) - b.begin();
        ans += (b_end - b_start);
    }

    cout << ans << "\n";



}