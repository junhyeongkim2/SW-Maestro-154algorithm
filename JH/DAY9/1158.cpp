#include <bits/stdc++.h>
using namespace std;


int n,k;
int arr [5001];

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    cin >> n >> k;

    for (int i = 0; i <n ; ++i) {
        arr[i] = i+1;
    }

    vector<int>v1;
    int allcnt=0;

    int cnt=0;
    while(true){
        for (int i = 0; i <n ; ++i) {
            if ( arr[i] !=0 ){
                cnt++;
            }
            if(cnt==k){
                arr[i]=0;
                cnt=0;
                v1.push_back(i);
                allcnt++;
            }
        }
        if(allcnt == n){
            break;
        }
    }

    cout << "<";
    for (int i = 0; i < v1.size(); ++i) {
        cout << v1[i]+1;
        if(i<v1.size()-1){
            cout << ", ";
        }
    }
    cout << ">";


}
