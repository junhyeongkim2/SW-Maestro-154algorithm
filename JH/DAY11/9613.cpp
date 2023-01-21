#include <bits/stdc++.h>
using namespace std;


int gcd(int a, int b){

    int c=  a%b;
    while(c!=0){
        a = b;
        b = c;
        c= a%b;
    }
    return b;

}



int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;

    while(t--){
        int n;
        vector<int>v1;
        long long int sum=0;
        cin >> n;
        for (int i = 0; i <n ; ++i) {
            int a;
            cin >> a;
            v1.push_back(a);
        }

        for (int i = 0; i <n ; ++i) {
            for (int j = i+1; j <n ; ++j) {
                //cout << v1[i] << " " << v1[j] << "\n";
                sum += gcd (v1[i], v1[j]);
            }
        }
        cout << sum <<"\n";

    }



}
