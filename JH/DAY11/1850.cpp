#include <bits/stdc++.h>
using namespace std;


long long int gcd(long long int a, long long int b){
    long long int c = a % b;
    while(c!=0){
        a = b;
        b = c;
        c = a%b;
    }
    return b;
}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long int a, b;
    cin >> a >> b;

    long long int result = gcd(a,b);
    //cout << result <<"\n";

    for (int i = 0; i <result ; ++i) {
        cout << 1;
    }

    cout << "\n";
    return 0;

}
