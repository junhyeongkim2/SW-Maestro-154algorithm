#import <bits/stdc++.h>
using namespace std;

long long int n;
long long int arr[4000002];

vector<long long int>v;

//에라토스테네스의 체로 소수 구하고 투포인터

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n;


    if(n==1){
        cout << 0;
        return 0;
    }else if (n==2){
        cout << 1;
        return 0;
    }

    for(int i = 2; i<= n;i++){
        arr[i]=i;
    }

    for(int i = 2 ; i <= sqrt(n); i++){
        if(arr[i]==0)continue;
        for(int j = i*i; j <= n; j+=i){
            arr[j]=0;
        }
    }

    for(int i = 2 ; i<=n; i++){
        if(arr[i]>0){
            v.push_back(i);
        }
    }


    long long int start = 0;
    long long int end = 0;
    long long int result = 0;
    long long int sum = v[0];

    while(start<=end&&end<= v.size()-1){
        //cout << start << " " << end << " " <<sum << "\n";
        if(sum<n){
            end++;
            sum += v[end];
        }else{
            sum -= v[start];
            start++;
        }

        if(sum == n ){
            result++;
        }

    }
    cout << result << "\n";


}