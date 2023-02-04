#import <bits/stdc++.h>
using namespace std;

int n,c;
vector<int> houses;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> c;

    for(int i = 0 ; i < n ; i++){
        int temp;
        cin >> temp;
        houses.push_back(temp);
    }

    sort(houses.begin(),houses.end());

    int start = 1;
    int end = houses[n-1] - houses[0];
    int result = 0;

    while(start<=end){
        int cnt = 1;
        int mid = (start+end)/2;
        int prev = houses[0];
        for(int i = 1 ; i < n; i++){
            if(houses[i]-prev >= mid){
                prev = houses[i];
                cnt ++;
            }
        }
        if(cnt>=c){
            result = mid;
            start = mid + 1 ;
        }else{
            end = mid - 1;
        }
    }

    cout << result << "\n";






}