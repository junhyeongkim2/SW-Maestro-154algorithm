#include <bits/stdc++.h>
using namespace std;


int gcd(int a, int b){
    int c = a%b;
    while(c!=0){
        a =b;
        b = c;
        c = a%b;
    }
    return b;
}

int lcm(int a, int b){

    return (a*b)/gcd(a,b);

}


int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int a,b;
    cin >> a >> b;
    cout << gcd(a,b) << "\n";
    cout << lcm(a,b);



}
